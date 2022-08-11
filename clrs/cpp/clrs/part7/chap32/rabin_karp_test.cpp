#include "rabin_karp.h"
#include <iostream>
using namespace std;
using namespace part7::chap32;

int main()
{

    RabinKarpSearch searcher("TEST");
    auto idx = searcher.Search(
        "THIS IS A TEST TEXT");

    cout << " Runing test " << idx;
    return !(idx == 10);
}