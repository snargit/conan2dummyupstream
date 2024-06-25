cmake_minimum_required(VERSION 3.24)
project(unittest CXX)
include(CMakePrintHelpers)
string(TOUPPER ${PROJECT_NAME} PRJ_PREFIX)

find_package(GTest CONFIG REQUIRED)
include_directories(${GTest_INCLUDE_DIRS})
include(GoogleTest)

set(${PRJ_PREFIX}_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(${PRJ_PREFIX}_SOURCES ${${PRJ_PREFIX}_SOURCE_DIR}/test.cpp)

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${${PRJ_PREFIX}_SOURCES})
source_group(TREE ${${PRJ_PREFIX}_SOURCE_DIR} PREFIX src FILES ${${PRJ_PREFIX}_SOURCES})
target_link_libraries(${PROJECT_NAME} PRIVATE GTest::gtest_main mytest)
cmake_print_properties(
    TARGETS GTest::gtest_main
    PROPERTIES IMPORTED_CONFIGURATIONS
)
if (WIN32)
    add_custom_command(TARGET ${PROJECT_NAME}
                       POST_BUILD
                       COMMAND ${CMAKE_COMMAND} -E copy_if_different $<TARGET_RUNTIME_DLLS:${PROJECT_NAME}> $<TARGET_FILE_DIR:${PROJECT_NAME}>
                       COMMAND_EXPAND_LISTS)
endif()
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
gtest_discover_tests(${PROJECT_NAME} DISCOVERY_MODE PRE_TEST)