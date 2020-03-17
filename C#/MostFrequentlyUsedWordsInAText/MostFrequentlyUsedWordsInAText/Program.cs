/*
 * Most frequently used words in a text - Codewars
 * Nilton Gomes Martins Junior
 * 14/03/2020
 * https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/csharp
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace MostFrequentlyUsedWordsInAText
{
    class Program
    {
        static void Main(string[] args)
        {
            var topWords = TopWords.Top3("  '''  ");
            foreach (var word in topWords)
            {
                Console.WriteLine(word);
            }
        }
    }

    public class TopWords
    {
        public static List<string> Top3(string s)
        {
            var wordList = Regex.Split(s, @"[^a-zA-Z']+").Select(w => Regex.Replace(w, @"^[\s']*$", "").ToLower()).Where(w => w != "").ToList();
            var wordFreq = wordList.GroupBy(w => w).ToDictionary(w => w.Key, w => w.Count());
            var topWords = wordFreq.OrderBy(w => w.Value).Reverse().Select(w => w.Key).Take(3).ToList();
            return topWords;
        }
    }
}
