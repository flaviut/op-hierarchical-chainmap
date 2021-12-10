#include <pybind11/pybind11.h>

#include <cstdint>
#include <algorithm>
#include <sstream>

using namespace pybind11::literals;
namespace py = pybind11;

struct CppChainMap {
    py::list maps;

    CppChainMap() {
        maps = py::list();
        this->maps.append(py::dict());
    }

    explicit CppChainMap(const py::args &maps) : CppChainMap(py::object(maps)) {}

    explicit CppChainMap(const py::object &maps) {
        if (py::len(maps) == 0) {
            this->maps = py::list();
            // always at least one map
            this->maps.append(py::dict());
        } else {
            this->maps = py::list(maps);
        }
    }

    CppChainMap copy() const {
        // New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]
        auto newMaps = py::list();
        for (int i = 0; i < this->maps.size(); ++i) {
            const auto &map = this->maps[i];
            if (i == 0) {
                newMaps.append(map.attr("copy")());
            } else {
                newMaps.append(map);
            }
        }
        return CppChainMap{newMaps};
    }

    CppChainMap newChild(py::object m) const {
        if (m.is_none()) {
            m = py::dict();
        }
        py::list args{};
        args.append(m);
        args.attr("extend")(this->maps);
        return CppChainMap(args);
    }

    py::object _getitem(const py::str &key) const {
        for (const auto &h: maps) {
            auto mapping = h.cast<py::dict>();
            if (mapping.contains(key)) {
                return mapping[key];
            }
        }
        throw pybind11::key_error(key);
    }

    void _setitem(const py::str &key, const py::object &value) {
        maps[0][key] = value;
    }

    void _delitem(const py::str &key) {
        if (!maps[0].contains(key)) {
            std::stringstream msg;
            msg << "Key not found in the first mapping: '" << key.cast<std::string>() << "'";
            throw pybind11::key_error(msg.str());
        }
        maps[0].attr("pop")(key);
    }

    py::object get(const std::string &key, const py::object &def) const {
        if (this->_contains(key)) {
            return this->_getitem(key);
        } else {
            return def;
        }
    }

    bool _contains(const py::str &key) const {
        for (const auto &mapping: maps) {
            if (mapping.contains(key)) {
                return true;
            }
        }
        return false;
    }

    /** flattens the chainmap into a single map */
    py::dict flattened() const {
        py::dict d{};
        for (size_t i = this->maps.size() - 1; i != SIZE_MAX; --i) {
            const py::dict &mapping = this->maps[i];
            d.attr("update")(mapping);
        }
        return d;
    }

    size_t _len() const {
        return py::len(flattened());
    }

    CppChainMap parents() const {
        return CppChainMap(this->maps[py::slice(1, this->maps.size(), 1)].cast<py::list>());
    }

    py::iterator _iter() const {
        return py::iter(this->flattened());
    }

    py::object items() const {
        return this->flattened().attr("items")();
    }

    py::object keys() const {
        return this->flattened().attr("keys")();
    }

    py::object values() const {
        return this->flattened().attr("values")();
    }

    bool _eq(const py::object &other) const {
        return py::dict(other.attr("items")()).equal(this->flattened());
    }

    py::list &attrMaps() {
        return maps;
    }
};

struct CppHierarchicalChainMap : public CppChainMap {
    using CppChainMap::CppChainMap;

    py::dict deepDict(const py::handle &root);
};


static py::object hierarchyForKey(const py::str &key, const py::handle &chain) {
    py::list wrappedMappings{};
    const auto &maps = chain.cast<CppChainMap>().maps;
    for (const auto &mapping: maps) {
        if (mapping.contains(key) && !mapping[key].is_none()) {
            wrappedMappings.attr("push")(mapping[key]);
        } else {
            wrappedMappings.attr("push")(py::dict());
        }
    }
    return py::cast(CppHierarchicalChainMap(wrappedMappings));
}

static py::handle getNext(const py::str &key, const py::handle &node, bool onlyLocal = false) {
    if (py::isinstance<py::dict>(node)) {
        return node[key];
    } else if (onlyLocal && !node.cast<CppChainMap>().maps[0].contains(key)) {
        throw py::key_error(key);
    } else {
        return hierarchyForKey(key, node);
    }
}

PYBIND11_MODULE(op_hierarchical_chainmap, m) {
    py::class_<CppChainMap>(m, "ChainMap")
            .def(py::init<>())
            .def(py::init<const py::args &>())
            .def("__copy__", &CppChainMap::copy)
            .def("copy", &CppChainMap::copy)
            .def("new_child", &CppChainMap::newChild, py::arg("m") = py::none())
            .def(py::pickle(
                    [](const CppChainMap &p) { // __getstate__
                        /* Return a tuple that fully encodes the state of the object */
                        return py::make_tuple(p.maps);
                    },
                    [](const py::tuple &t) { // __setstate__
                        if (t.size() != 1)
                            throw std::runtime_error("Invalid state!");
                        return CppChainMap(t[0].cast<py::list>());
                    }
            ))
            .def("__getitem__", &CppChainMap::_getitem)
            .def("__setitem__", &CppChainMap::_setitem)
            .def("__delitem__", &CppChainMap::_delitem)
            .def("__contains__", &CppChainMap::_contains)
            .def("__len__", &CppChainMap::_len)
                    // don't need weak references here because we copy all the data &
                    // create the iterators from a temporary object
            .def("__iter__", &CppChainMap::_iter)
            .def("items", &CppChainMap::items)
            .def("keys", &CppChainMap::keys)
            .def("values", &CppChainMap::values)
            .def("__eq__", &CppChainMap::_eq)
            .def("flatten", &CppChainMap::flattened)
            .def("get", &CppChainMap::get, py::arg("key"), py::arg("default") = py::none())
            .def_property_readonly("parents", &CppChainMap::parents)
            .def_property_readonly("maps", &CppChainMap::attrMaps);
    py::class_<CppHierarchicalChainMap, CppChainMap>(m, "HierarchicalChainMap")
            .def(py::init<>())
            .def(py::init<const py::args &>())
            .def("deep_dict", &CppHierarchicalChainMap::deepDict, py::arg("root") = py::none());

    m.def("get_next", &getNext, py::arg("key"), py::arg("node"), py::arg("only_local") = false);
    m.def("hierarchy_for_key", &hierarchyForKey);

}

py::dict CppHierarchicalChainMap::deepDict(const py::handle &root) {
    if (root.is_none()) {
        return deepDict(py::cast(this));
    }

    py::dict result{};
    for (const auto &item: py::iter(root)) {
        static const auto int0 = py::int_(0);
        static const auto int1 = py::int_(1);
        const py::str &key = item[int0].cast<py::str>();
        const py::handle &value = item[int1];

        if (py::isinstance<py::dict>(value)) {
            result[key] = deepDict(getNext(key, root));
        } else {
            result[key] = value;
        }
    }
    return result;
}
