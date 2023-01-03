cmake_minimum_required(VERSION 3.23)
project(PkgTest)

find_package(mytest CONFIG REQUIRED)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} mytest::mytest)
