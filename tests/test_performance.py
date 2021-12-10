import timeit

from octoprint_settings import PyHierarchicalChainMap, example_object
from op_hierarchical_chainmap import \
    HierarchicalChainMap as CppHierarchicalChainMap


def test_performance():
    def create_test(HierarchicalChainMap):
        cm = HierarchicalChainMap({}, example_object)
        return lambda: cm.deep_dict(None)

    cpp_time = timeit.repeat(create_test(CppHierarchicalChainMap), number=100000)
    py_time = timeit.repeat(create_test(PyHierarchicalChainMap), number=10000) * 10
    # make sure the c++ version is at least 80x faster than the python version
    assert cpp_time * 80 < py_time
