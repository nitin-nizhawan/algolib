target_sources(clrs 
     PRIVATE string_matching.cpp rabin_karp.cpp
     PUBLIC string_matching.h rabin_karp.h
)
target_sources(clrs_static 
     PRIVATE string_matching.cpp rabin_karp.cpp
     PUBLIC string_matching.h rabin_karp.h
)
target_sources(
    stringmatchingtest
    PRIVATE string_matching_test.cpp
)
target_sources(
    rabinkarptest
    PRIVATE rabin_karp_test.cpp
)