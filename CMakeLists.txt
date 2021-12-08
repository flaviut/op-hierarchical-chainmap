cmake_minimum_required(VERSION 3.16)
project(op_hierarchical_chainmap)

include(cmake/CPM.cmake)

CPMAddPackage(
        NAME Format.cmake
        VERSION 1.7.0
        GITHUB_REPOSITORY TheLartians/Format.cmake
        OPTIONS "FORMAT_SKIP_CMAKE YES"
)

set(CMAKE_CXX_STANDARD 14)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(op_hierarchical_chainmap
        src/main.cpp
        )