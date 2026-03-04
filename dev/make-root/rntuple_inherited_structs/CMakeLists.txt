cmake_minimum_required(VERSION 3.20)

project(rntuple-inherited-structs)

find_package(ROOT 6.36.0 REQUIRED)

add_executable(gen-test-data
    main.cpp
)

target_link_libraries(gen-test-data
    ROOT::Core
    ROOT::RIO
    ROOT::ROOTNTuple
)

ROOT_GENERATE_DICTIONARY(test_rntpl_dict
    structs.h
    LINKDEF LinkDef.h
    MODULE gen-test-data
)
