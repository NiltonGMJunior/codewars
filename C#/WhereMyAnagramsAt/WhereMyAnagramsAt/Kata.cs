using System;
using System.Collections.Generic;
using System.Linq;

namespace WhereMyAnagramsAt
{
    public static class Kata
    {
        public static List<string> Anagrams(string word, List<string> words)
        {
            return words.Where(w => AreAnagrams(w, word)).ToList();
        }

        public static bool AreAnagrams(string word1, string word2)
        {
            var chars1 = word1.ToLower().ToList();
            var chars2 = word2.ToLower().ToList();
            chars1.Sort();
            chars2.Sort();
            return chars1.SequenceEqual(chars2);
        }
    }
}