#include <string>
#include <memory>

using namespace std;

namespace part7
{
    namespace chap32
    {
        class RollingHash
        {
            int hash;
            int M = 9973;
            int B = 256;
            int H = 1;

        public:
            RollingHash(string s, int len);
            int val();
            int slide(const string &s, int i, int len);
        };

        class RabinKarpSearch
        {

            string needle;
            unique_ptr<RollingHash> phash;
            bool IsAt(const string &haystack, const string &needle, int pos) const;

        public:
            RabinKarpSearch(const string &pattern);
            int Search(const string &haystack) const;
        };
    }
}
