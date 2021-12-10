# op_hierarchical_chainmap

A faster HierarchicalChainMap built for Octoprint with
[pybind11](https://github.com/pybind/pybind11). This requires Python 3.6+.

## Usage

```console
$ git clone git@github.com:flaviut/op-hierarchical-chainmap.git
$ cd op-hierarchical-chainmap
$ virtualenv venv
$ source venv/bin/activate
$ pip install .
$ pip install pytest
$ pytest  # run chainmap unit tests
$ python ./tests/test.py  # run HierarchicalChainMap.deep_dict() performance tests
```

## Development

Clion was used in the development of this program. You can open this as a Clion project using the `CMakeLists.txt` file.
