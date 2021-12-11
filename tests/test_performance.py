import timeit

import pytest
from octoprint_settings import PyHierarchicalChainMap, example_chain

from op_hierarchical_chainmap import \
    HierarchicalChainMap as CppHierarchicalChainMap


@pytest.mark.skip
def test_performance_deepdict():
    def create_test(HierarchicalChainMap):
        cm = HierarchicalChainMap(*example_chain)
        return lambda: cm.deep_dict()

    cpp_time = min(timeit.repeat(create_test(CppHierarchicalChainMap), number=20000))
    py_time = min(timeit.repeat(create_test(PyHierarchicalChainMap), number=2000)) * 10
    print(cpp_time, py_time)
    # make sure the c++ version is at least 8x faster than the python version
    assert cpp_time * 8 < py_time

if __name__ == '__main__':
    test_performance_deepdict()
