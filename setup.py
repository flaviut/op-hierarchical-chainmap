# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import (ParallelCompile, Pybind11Extension,
                                    build_ext)
from setuptools import setup

__version__ = "0.0.1"

# Optional multithreaded build
ParallelCompile("NPY_NUM_BUILD_JOBS").install()

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension(
        "op_hierarchical_chainmap._ext",
        ["src/main.cpp"],
        extra_compile_args=["-g"],
    ),
]
packages = ['op_hierarchical_chainmap']

setup(
    name="op_hierarchical_chainmap",
    version=__version__,
    author="Flaviu Tamas",
    author_email="me@flaviutamas.com",
    url="https://github.com/flaviut/op-hierarchical-chainmap",
    description="A faster, native, replacement for Octoprint's HierarchicalChainMap",
    long_description="",
    ext_modules=ext_modules,
    packages=packages,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
