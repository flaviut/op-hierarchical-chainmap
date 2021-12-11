cmake_minimum_required(VERSION 3.16)
project(op_hierarchical_chainmap_cppext)

include(cmake/CPM.cmake)

CPMAddPackage(
        NAME Format.cmake
        VERSION 1.7.0
        GITHUB_REPOSITORY TheLartians/Format.cmake
        OPTIONS "FORMAT_SKIP_CMAKE YES"
)

set(CMAKE_CXX_STANDARD 17 CACHE STRING "C++ version selection")  # or 11, 14, 17, 20
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # optional, ensure standard is supported
set(CMAKE_CXX_EXTENSIONS OFF)  # optional, keep compiler extensions off

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(op_hierarchical_chainmap_cppext
        src/main.cpp
        )
