#include <pybind11/pybind11.h>

#include <algorithm>
#include <sstream>

using namespace pybind11::literals;
namespace py = pybind11;

struct CppChainMap {
    py::list maps;

    CppChainMap() {
        // always at least one map
        maps = py::list(py::dict());
    }

    explicit CppChainMap(const py::args &maps) : CppChainMap() {
        this->maps = py::list(maps);
    }

    explicit CppChainMap(const py::object &maps) : CppChainMap() {
        this->maps = py::list(maps);
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
        for (ssize_t i = py::len(this->maps) - 1; i >= 0; --i) {
            const auto &mapping = this->maps[i].cast<py::dict>();
            d.attr("update")(mapping);
        }
        return d;
    }

    size_t _len() const {
        return py::len(flattened());
    }

    CppChainMap parents() const {
        return CppChainMap(this->maps[py::slice(1, -1, 1)].cast<py::object>());
    }

    py::iterator _iter() const {
        return py::iter(this->flattened());
    }

    py::list &attrMaps() {
        return maps;
    }
};

struct CppHierarchicalChainMap : public CppChainMap {
    using CppChainMap::CppChainMap;

    py::dict deepDict(const py::handle &root);
    py::object
};


PYBIND11_MODULE(op_hierarchical_chainmap, m) {
    py::class_<CppChainMap>(m, "ChainMap")
            .def(py::init<>())
            .def(py::init<py::object>())
            .def(py::init<py::args>())
            .def("__getitem__", &CppChainMap::_getitem)
            .def("__setitem__", &CppChainMap::_setitem)
            .def("__delitem__", &CppChainMap::_delitem)
            .def("__contains__", &CppChainMap::_contains)
            .def("__len__", &CppChainMap::_len)
            .def("__iter__", &CppChainMap::_iter)
            .def("flatten", &CppChainMap::flattened)
            .def("get", &CppChainMap::get)
            .def_property_readonly("parents", &CppChainMap::parents)
            .def_property_readonly("maps", &CppChainMap::attrMaps);
    py::class_<CppHierarchicalChainMap>(m, "HierarchicalChainMap")
            .def(py::init<>())
            .def(py::init<py::object>())
            .def(py::init<py::args>())
            .def("__getitem__", &CppHierarchicalChainMap::_getitem)
            .def("__setitem__", &CppHierarchicalChainMap::_setitem)
            .def("__delitem__", &CppHierarchicalChainMap::_delitem)
            .def("__contains__", &CppHierarchicalChainMap::_contains)
            .def("__len__", &CppHierarchicalChainMap::_len)
            .def("__iter__", &CppHierarchicalChainMap::_iter)
            .def("flatten", &CppHierarchicalChainMap::flattened)
            .def("get", &CppHierarchicalChainMap::get)
            .def_property_readonly("parents", &CppHierarchicalChainMap::parents)
            .def_property_readonly("maps", &CppHierarchicalChainMap::attrMaps)
            .def("deep_dict", &CppHierarchicalChainMap::deepDict, py::arg("root") = py::none());

}

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