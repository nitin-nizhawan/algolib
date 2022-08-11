#include "rabin_karp.h"

namespace part7
{
    namespace chap32
    {

        RollingHash::RollingHash(string s, int len)
        {
            hash = 0;
            for (int i = 0; i < len - 1; i++)
            {
                H = (H * B) % M;
            }
            for (int i = 0; i < len; i++)
            {
                hash = ((hash * B) % M + (s[i] - '\0')) % M;
            }
        }
        int RollingHash::val()
        {
            return hash;
        }
        int RollingHash::slide(const string &s, int i, int len)
        {
            auto cprev = s[i - 1] - '\0';
            auto cnow = s[i + len - 1] - '\0';
            auto additive_inverse = M - (cprev * H) % M;
            hash = (((hash + additive_inverse) * B) % M + cnow) % M;
            return hash;
        }

        bool RabinKarpSearch::IsAt(const string &haystack, const string &needle, int pos) const
        {
            if (pos + needle.length() > haystack.length())
            {
                return false;
            }
            for (int i = 0; i < needle.length(); i++)
            {
                if (needle[i] != haystack[i + pos])
                {
                    return false;
                }
            }
            return true;
        }

        RabinKarpSearch::RabinKarpSearch(const string &pattern) : needle(pattern), phash(new RollingHash(pattern, pattern.length())) {}
        int RabinKarpSearch::Search(const string &haystack) const
        {
            if (needle == "")
            {
                return 0;
            }
            if (haystack.length() < needle.length())
            {
                return -1;
            }
            // calc needle hash
            int hash = 0;
            int rollinghash = 0;
            unique_ptr<RollingHash> thash(new RollingHash(haystack, needle.length()));

            if (phash->val() == thash->val() && IsAt(haystack, needle, 0))
            {
                return 0;
            }
            //  Console.WriteLine("hash="+hash+" , rhash="+rollinghash);
            for (int i = 1; i < haystack.length() - needle.length() + 1; i++)
            {
                thash->slide(haystack, i, needle.length());
                //   Console.WriteLine("hash="+hash+" , rhash="+rollinghash+ ", i="+i);
                if (phash->val() == thash->val() && IsAt(haystack, needle, i))
                {
                    return i;
                }
            }
            return -1;
        }

    }
}
