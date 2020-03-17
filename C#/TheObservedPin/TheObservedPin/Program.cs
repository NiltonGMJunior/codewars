/*
 * The observed PIN - Codewars
 * Nilton Gomes Martins Junior
 * 14/03/2020
 * https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/csharp
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace TheObservedPin
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var s in Kata.GetPINs("11"))
            {
                Console.WriteLine(s);
            }
        }
    }

    public class Kata
    {
        public static List<string> GetPINs(string observed)
        {
            var keyMap = new Dictionary<string, List<string>>
            {
                { "0", new List<string> { "0", "8" } },
                { "1", new List<string> {"1", "2", "4" } },
                { "2", new List<string> {"1", "2", "3", "5" } },
                { "3", new List<string> {"2", "3", "6" } },
                { "4", new List<string> {"1", "4", "5", "7" } },
                { "5", new List<string> {"2", "4", "5", "6", "8" } },
                { "6", new List<string> {"3", "5", "6", "9" } },
                { "7", new List<string> {"4", "7", "8" } },
                { "8", new List<string> {"0", "5", "7", "8", "9" } },
                { "9", new List<string> {"6", "8", "9" } },
            } ;

            var combinations = new List<string> { "" };
            foreach (var c in observed)
            {
                combinations = GetCombinations(combinations, keyMap[c.ToString()]);
            }

            return combinations.Distinct().ToList();
        }

        public static List<string> GetCombinations(List<string> listA, List<string> listB)
        {
            var combinations = new List<string>();
            foreach (var strA in listA)
            {
                foreach (var strB in listB)
                {
                    combinations.Add(strA + strB);
                }
            }

            return combinations.Distinct().ToList();
        }
    }

}
