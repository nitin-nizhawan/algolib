#include "string_matching.h"
#include<iostream>
using namespace std;
using namespace part7::chap32;

int main(){

    auto idx = StringMatching::RabinKarp(
        "TEST",
        "THIS IS A TEST TEXT"
    );
    
    cout<<" Runing test "<<idx;
    return !(idx == 10);
}