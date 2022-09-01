namespace CLRS.Tests;
using CLRS.Part7.Chap32;

public class StringMatchingTest
{
    [Fact]
    public void TestRabinKarp()
    {
         //Assert.Equal(10,StringMatching.RabinKarp("TEST","THIS IS A TEST TEXT"));
    }

    [Fact]
    public void TestKnuthMorisPratt(){
        // Assert.True(StringMatching.KnuthMorrisPratt("nitin","nitin") == 0,"shoudl be true");
    }

     [Fact]
    public void TestKnuthMorisPrattMultipleText(){
         var searcher = new KMPSearch("abcabcacab");
       //  var first = searcher.Search("babcbabcabcaabcabcabcacabc");
         var first = searcher.Search("babcbabcabcbabcabcabcacabc");
         Assert.Equal(15, first);
    }
}
