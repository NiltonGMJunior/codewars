/*
 * Where my anagrams at? - Codewars
 * Nilton Gomes Martins Junior
 * 07/03/2020
 * https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/csharp
 */

using System;
using System.Collections.Generic;

namespace WhereMyAnagramsAt
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = "abba";
            var b = new List<string> {"aabb", "abcd", "bbaa", "dada"};
            foreach (var anagram in Kata.Anagrams(a, b))
            {
                Console.WriteLine(anagram);
            }
        }
    }
}
