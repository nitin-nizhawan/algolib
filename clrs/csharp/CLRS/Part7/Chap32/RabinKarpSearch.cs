namespace CLRS.Part7.Chap32;

public class RabinKarpSearch {
    private string needle;
    private RollingHash phash;
    public RabinKarpSearch(string pattern){
	    this.needle = pattern;
	    this.phash = new RollingHash(pattern,pattern.Length);

    }
    public int Search(string haystack){
        if(needle==""){
            return 0;
        }
        if(haystack.Length < needle.Length){
            return -1;
        }
        // calc needle hash
        int hash = 0;
        int rollinghash =0;
        var thash = new RollingHash(haystack,needle.Length);
        
        if(phash.val()==thash.val() && IsAt(haystack,needle,0)){
            return 0;
        }
       //  Console.WriteLine("hash="+hash+" , rhash="+rollinghash);
        for(int i=1;i<haystack.Length-needle.Length + 1;i++){
            thash.slide(haystack,i,needle.Length);
          //   Console.WriteLine("hash="+hash+" , rhash="+rollinghash+ ", i="+i);
            if(phash.val()==thash.val() && IsAt(haystack,needle,i)){
                return i;
            }
                
        }
        return -1;
    }
    private bool IsAt(string haystack, string needle, int pos){
        if(pos + needle.Length > haystack.Length){
            return false;
        }
        for(int i=0;i<needle.Length;i++){
            if(needle[i]!=haystack[i+pos]){
                return false;
            }
        }
        return true;
    }

 private class RollingHash {
        int hash;
        int M = 9973;
        int B =  256;
        int H = 1;
        public RollingHash(string s, int len){
            hash = 0;
            for (int i = 0; i < len-1; i++){
               H = (H*B)%M;
            }
            for(int i=0;i<len;i++){
                hash = ((hash*B)%M + (s[i]-'\0'))%M;
            }
        }
        public int val(){
            return hash;
        }
        public int slide(string s,int i,int len){
            var cprev = s[i-1] - '\0';
            var cnow = s[i+len -1] -'\0';
            var additive_inverse = M - (cprev*H)%M;
            hash = (((hash + additive_inverse)*B)%M + cnow)%M;
            return hash;
        }
    }
}
