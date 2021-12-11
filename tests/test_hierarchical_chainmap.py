from octoprint_settings import PyHierarchicalChainMap, example_chain

from op_hierarchical_chainmap import HierarchicalChainMap


def test_deep_dict():
    assert HierarchicalChainMap(*example_chain).deep_dict() == \
           PyHierarchicalChainMap(*example_chain).deep_dict()


def test_realistic_get():
    cm = HierarchicalChainMap(*example_chain)
    pcm = PyHierarchicalChainMap(*example_chain)
    print(pcm.get_by_path(["accessControl"], merged=True))
    print(cm.get_by_path(["accessControl"], merged=True))
    assert cm.get_by_path(["webcam", "timelapse"], merged=True) == {
        "type": "off", "options": {}, "postRoll": 0, "fps": 25}
