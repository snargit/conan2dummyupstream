cmake_minimum_required(VERSION 3.23)
project(unittest CXX)

string(TOUPPER ${PROJECT_NAME} PRJ_PREFIX)

find_package(GTest CONFIG REQUIRED)
include_directories(${GTest_INCLUDE_DIRS})
include(GoogleTest)

set(${PRJ_PREFIX}_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(${PRJ_PREFIX}_SOURCES ${${PRJ_PREFIX}_SOURCE_DIR}/test.cpp)

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${${PRJ_PREFIX}_SOURCES})
source_group(TREE ${${PRJ_PREFIX}_SOURCE_DIR} PREFIX src FILES ${${PRJ_PREFIX}_SOURCES})
target_link_libraries(${PROJECT_NAME} GTest::gtest GTest::gtest_main mytest)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
get_target_property(xx Gtest::gtest LIBRARY_OUTPUT_DIRECTORY)
gtest_discover_tests(${PROJECT_NAME})