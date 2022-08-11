#include "string_matching.h"
#include "rabin_karp.h"
#include <iostream>
using namespace std;

int part7::chap32::
    StringMatching::RabinKarp(string needle, string haystack)
{
   RabinKarpSearch searcher(needle);
   return searcher.Search(haystack);
}
