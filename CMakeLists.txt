cmake_minimum_required(VERSION 3.10)
project(CppUnitTestGen)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Add source files
add_executable(test_main main.cpp tests/test_main.cpp)

# GoogleTest location (update the path if needed)
add_subdirectory("D:\ googletest-main\ googletest-main" "googletest-build")

# Link GoogleTest libraries
target_link_libraries(test_main gtest gtest_main)
target_include_directories(test_main PRIVATE "D:/googletest-main/googletest/include")
