from op_hierarchical_chainmap import HierarchicalChainMap


def test_insert_map():
    cm = HierarchicalChainMap({"as": 1, "b": 2})
    assert cm.flatten() == {"as": 1, "b": 2}
    cm.maps.insert(1, {"c": 3})
    assert cm.flatten() == {"as": 1, "b": 2, "c": 3}
