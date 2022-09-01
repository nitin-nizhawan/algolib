namespace CLRS.Part7.Chap32;

public class KMPSearch {
        private int[] lps;
        private string pattern;
        public KMPSearch(string pattern){
        //    0 0 1 2 
        //    a b a b b b a b a b a b
            this.pattern = pattern;
            lps = new int[pattern.Length];
            lps[0]=0;
            for(int i=1;i<pattern.Length;i++){
                lps[i] = 0;
                var lastPrefixLen = lps[i-1];
                while(lastPrefixLen > 0 && pattern[i] != pattern[lastPrefixLen]){
                   lastPrefixLen = lps[lastPrefixLen-1];                   
                }  
                if(pattern[i] == pattern[lastPrefixLen]){
                   lps[i] = lastPrefixLen+1;
                }
            
            }
           lps = new int[]{0,0,-1,0,0,-1,4,-1,0,1};
           Console.WriteLine(string.Join(",",lps));
        }
        public int Search(string haystack){
            if(lps.Length < 1) return 0;
            int i=0;
            int j=0;
            int count = 0;
            while(i<haystack.Length){
                Console.WriteLine($"Matching parttern[{j}] with text[{i}] : {haystack[i]==pattern[j]} , {++count}");
                if(haystack[i]==pattern[j]){
                    i++;
                    j++;
                } else if(j==0 || this.lps[j-1] == -1){
                    i++;
                    j=0;
                } else {
                    j = this.lps[j-1];
                }               
                if(j == pattern.Length){
                    return i - pattern.Length;
                }
            }
            return -1;
        }
        
    }
 
