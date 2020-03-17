/*
 * Is my friend cheating? - Codewars
 * Nilton Gomes Martins Junior
 * 14/03/2020
 * https://www.codewars.com/kata/5547cc7dcad755e480000004/train/csharp
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace IsMyFriendCheating
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var pair in RemovedNumbers.removNb(26))
            {
                Console.WriteLine($"{pair[0]} {pair[1]}");
            }
        }
    }

    public class RemovedNumbers
    {
        public static List<long[]> removNb(long n)
        {
            var pairs = new HashSet<long[]>();
            long a;
            for (long b = 1; b < n; b++)
            {
                if ((n * (n + 1) - 2 * b) % (2 * (b + 1)) == 0)
                {
                    a = (n * (n + 1) - 2 * b) / (2 * (b + 1));
                    if (a < n && !pairs.Contains(new long[] { a, b })) //   TODO: Figure out how to avoid adding the same pair of numbers.
                    {
                        pairs.Add(new long[] { a, b });
                        pairs.Add(new long[] { b, a });
                    }
                }
            }

            return pairs.ToList();
        }
    }
}
