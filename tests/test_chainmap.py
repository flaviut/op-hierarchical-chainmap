from collections import OrderedDict, UserDict

import copy
import pickle
import unittest
from op_hierarchical_chainmap import ChainMap

class TestChainMap(unittest.TestCase):

    def test_basics(self):
        c = ChainMap()
        c['a'] = 1
        c['b'] = 2
        d = c.new_child()
        d['b'] = 20
        d['c'] = 30
        self.assertEqual(d.maps, [{'b':20, 'c':30}, {'a':1, 'b':2}])  # check internal state
        self.assertEqual(d.items(), dict(a=1, b=20, c=30).items())    # check items/iter/getitem
        self.assertEqual(len(d), 3)                                   # check len
        for key in 'abc':                                             # check contains
            self.assertIn(key, d)
        for k, v in dict(a=1, b=20, c=30, z=100).items():             # check get
            self.assertEqual(d.get(k, 100), v)

        del d['b']                                                    # unmask a value
        self.assertEqual(d.maps, [{'c':30}, {'a':1, 'b':2}])          # check internal state
        self.assertEqual(d.items(), dict(a=1, b=2, c=30).items())     # check items/iter/getitem
        self.assertEqual(len(d), 3)                                   # check len
        for key in 'abc':                                             # check contains
            self.assertIn(key, d)
        for k, v in dict(a=1, b=2, c=30, z=100).items():              # check get
            self.assertEqual(d.get(k, 100), v)

        for e in d.copy(), copy.copy(d):                               # check shallow copies
            self.assertEqual(d, e)
            self.assertEqual(d.maps, e.maps)
            self.assertIsNot(d, e)
            self.assertIsNot(d.maps[0], e.maps[0])
            for m1, m2 in zip(d.maps[1:], e.maps[1:]):
                self.assertIs(m1, m2)

        # check deep copies
        # pybind11 doesn't seem to support pickle v0 & v1
        for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
            e = pickle.loads(pickle.dumps(d, proto))
            self.assertEqual(d, e)
            self.assertEqual(d.maps, e.maps)
            self.assertIsNot(d, e)
            for m1, m2 in zip(d.maps, e.maps):
                self.assertIsNot(m1, m2, e)
        for e in [copy.deepcopy(d),
                  ]:
            self.assertEqual(d, e)
            self.assertEqual(d.maps, e.maps)
            self.assertIsNot(d, e)
            for m1, m2 in zip(d.maps, e.maps):
                self.assertIsNot(m1, m2, e)

        f = d.new_child()
        f['b'] = 5
        self.assertEqual(f.maps, [{'b': 5}, {'c':30}, {'a':1, 'b':2}])
        self.assertEqual(f.parents.maps, [{'c':30}, {'a':1, 'b':2}])   # check parents
        self.assertEqual(f['b'], 5)                                    # find first in chain
        self.assertEqual(f.parents['b'], 2)                            # look beyond maps[0]

    def test_ordering(self):
        # Combined order matches a series of dict updates from last to first.
        # This test relies on the ordering of the underlying dicts.

        baseline = {'music': 'bach', 'art': 'rembrandt'}
        adjustments = {'art': 'van gogh', 'opera': 'carmen'}

        cm = ChainMap(adjustments, baseline)

        combined = baseline.copy()
        combined.update(adjustments)

        self.assertEqual(list(combined.items()), list(cm.items()))

    def test_constructor(self):
        self.assertEqual(ChainMap().maps, [{}])                        # no-args --> one new dict
        self.assertEqual(ChainMap({1:2}).maps, [{1:2}])                # 1 arg --> list

    def test_bool(self):
        self.assertFalse(ChainMap())
        self.assertFalse(ChainMap({}, {}))
        self.assertTrue(ChainMap({1:2}, {}))
        self.assertTrue(ChainMap({}, {1:2}))
