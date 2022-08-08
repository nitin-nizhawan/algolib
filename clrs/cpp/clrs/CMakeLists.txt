cmake_minimum_required(VERSION 3.13)

# set the project name
project(CLRS)

add_library(clrs SHARED "")
add_library(clrs_static "")

add_executable(stringmatchingtest "")
target_link_libraries(stringmatchingtest clrs)
add_executable(rabinkarptest "")
target_link_libraries(rabinkarptest clrs)



# include sources in subdirectories
add_subdirectory(part7/chap32)
enable_testing()
## define test to execute
add_test(NAME stringmatchingtest COMMAND stringmatchingtest)
add_test(NAME rabinkarptest COMMAND rabinkarptest)


