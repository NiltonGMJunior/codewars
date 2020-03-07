/*
 * Weight for weight - Codewars
 * Nilton Gomes Martins Junior
 * 07/03/02020
 * https://www.codewars.com/kata/55c6126177c9441a570000cc/train/csharp
 */
using System;
using System.Linq;
using System.Net.Mail;
using System.Security;
using static System.String;

namespace WeightForWeight
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(WeightSort.OrderWeight("56 65 74 100 99 68 86 180 90"));
        }
    }

    public class WeightSort
    {
        public static string OrderWeight(string strng)
        {
            var pairs = strng.Split().Select(s => new Tuple<string, int>(s, NumberWeight(s))).ToList();
            pairs.Sort(CompareWeights);
            return Join(' ', pairs.Select(t => t.Item1));
        }

        public static int NumberWeight(string num)
        {
            int sum = 0;
            foreach (var c in num)
                sum += c - '0';
            return sum;
        }

        public static int CompareWeights(Tuple<string, int> t1, Tuple<string, int> t2)
        {
            if (t1.Item2 == t2.Item2)
                return Compare(t1.Item1, t2.Item1, StringComparison.Ordinal);
            return t1.Item2 < t2.Item2 ? -1 : 1;
        }
    }
}
