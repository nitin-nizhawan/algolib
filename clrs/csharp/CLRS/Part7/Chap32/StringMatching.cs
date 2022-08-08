namespace CLRS.Part7.Chap32;
public class StringMatching
{
  public static int RabinKarp(string needle, string haystack){
	   var searcher = new RabinKarpSearch(needle);
	   return searcher.Search(haystack);
  }

  public static int KnuthMorrisPratt(string needle, string haystack){
	  var searcher = new KMPSearch(needle);
        return searcher.Search(haystack);
   }
}
