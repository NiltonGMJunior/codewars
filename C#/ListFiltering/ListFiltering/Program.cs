/*
 * List Filtering - Codewars
 * Nilton Gomes Martins Junior
 * 29/02/2020
 * https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/csharp
 */

using System;
using System.Collections.Generic;

namespace ListFiltering
{
    class Program
    {
        static void Main(string[] args)
        {
            var testList = new List<object>() {1, 2, "a", "b"};
            foreach (int i in ListFilterer.GetIntegersFromList(testList))
            {
                Console.WriteLine(i);
            }
        }
    }
}
