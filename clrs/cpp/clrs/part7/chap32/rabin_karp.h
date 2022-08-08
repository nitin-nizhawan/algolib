#include<string>
using namespace std;

namespace part7{
    namespace chap32{
class RollingHash {
        int hash;
        int M = 9973;
        int B = 256;
        int H = 1;
        public: 
        RollingHash(string s, int len);
        int val();
        int slide(string s,int i,int len);
};

    class RabinKarpSearch {

    string needle;
    RollingHash phash;
    bool IsAt(string haystack, string needle, int pos);
    public:
    RabinKarpSearch(string pattern);
    int Search(string haystack);
};
    }
}

