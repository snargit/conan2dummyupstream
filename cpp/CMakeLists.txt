cmake_minimum_required(VERSION 3.24)
#set(CMAKE_PROJECT_TOP_LEVEL_INCLUDES "conan_provider.cmake")
project(mytest CXX)
set(CMAKE_MESSAGE_LOG_LEVEL DEBUG)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
include(GenerateExportHeader)
include(CTest)

if (${CMAKE_CURRENT_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
message(FATAL_ERROR “In-source builds not allowed! Create a build directory and run CMake from there.” )
endif()

string(TOUPPER ${PROJECT_NAME} UPCASE_PRJ_NAME)
string(REPLACE "-" "_" PRJ_PREFIX ${UPCASE_PRJ_NAME})

set(${PRJ_PREFIX}_VERSION_MAJOR 0)
set(${PRJ_PREFIX}_VERSION_MINOR 1)
set(${PRJ_PREFIX}_VERSION_PATCH 0)
set(${PRJ_PREFIX}_VERSION
    "${${PRJ_PREFIX}_VERSION_MAJOR}.${${PRJ_PREFIX}_VERSION_MINOR}.${${PRJ_PREFIX}_VERSION_PATCH}")

set(${PRJ_PREFIX}_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(${PRJ_PREFIX}_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)

set(${PRJ_PREFIX}_PUBLIC_HEADERS ${${PRJ_PREFIX}_INCLUDE_DIR}/mytest/mytest.hpp)

set(${PRJ_PREFIX}_SOURCES ${${PRJ_PREFIX}_SOURCE_DIR}/mytest.cpp)

source_group(TREE ${${PRJ_PREFIX}_INCLUDE_DIR} PREFIX include FILES ${${PRJ_PREFIX}_PUBLIC_HEADERS})
source_group(TREE ${${PRJ_PREFIX}_SOURCE_DIR} PREFIX src FILES ${${PRJ_PREFIX}_SOURCES})

add_library(${PROJECT_NAME})
generate_export_header(${PROJECT_NAME}
                       EXPORT_FILE_NAME ${${PRJ_PREFIX}_INCLUDE_DIR}/mytest/spec.hpp)
target_sources(${PROJECT_NAME} PRIVATE ${${PRJ_PREFIX}_SOURCES})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS BASE_DIRS ${${PRJ_PREFIX}_INCLUDE_DIR}
                                               FILES ${${PRJ_PREFIX}_PUBLIC_HEADERS})
target_include_directories(${PROJECT_NAME} PUBLIC ${${PRJ_PREFIX}_INCLUDE_DIR})
target_include_directories(${PROJECT_NAME} PRIVATE ${${PRJ_PREFIX}_SOURCE_DIR})
target_compile_definitions(${PROJECT_NAME} PRIVATE BUILDING_MYTEST)

set_property(TARGET ${PROJECT_NAME} PROPERTY VERSION ${${PRJ_PREFIX}_VERSION})
set_property(TARGET ${PROJECT_NAME} PROPERTY SOVERSION ${${PRJ_PREFIX}_VERSION_MAJOR})

if (NOT BUILD_TESTING STREQUAL OFF)
    enable_testing()
    add_subdirectory(test)
endif()

install(TARGETS ${PROJECT_NAME} FILE_SET HEADERS)
install(FILES ${${PRJ_PREFIX}_INCLUDE_DIR}/mytest/spec.hpp
              DESTINATION include/${PROJECT_NAME})
