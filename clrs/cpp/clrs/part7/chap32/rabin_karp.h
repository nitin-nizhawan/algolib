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
        
        /**
         * @brief this class implements
         * rabin karp search
         * 
         */
        class RabinKarpSearch
        {

            string needle;
            unique_ptr<RollingHash> phash;
            bool IsAt(const string &haystack, const string &needle, int pos) const;

        public:
            /**
             * @brief Construct a new Rabin Karp Search object
             * Creates an instance of rabing  karp searcher
             * for a given pattern. This instance
             * can be used to search on any number of texts
             * @param pattern the pattern which has to be searched
             */
            RabinKarpSearch(const string &pattern);
            /**
             * @brief method to search in a text
             * This method will search for the pattern with
             * which this instance of searcher was created.
             * It returns the first occurance of the instance
             * @param haystack the text which has to be searched
             * @return int index of the pattern. If pattern is not found
             * then -1 is returned
             */
            int Search(const string &haystack) const;
        };
    }
}
