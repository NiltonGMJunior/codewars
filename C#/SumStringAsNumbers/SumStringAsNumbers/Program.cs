/*
 * Sum Strings as Numbers - Codewars
 * Nilton Gomes Martins Junior
 * 29/03/2020
 * https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/csharp
 */

using System;
using System.Text.RegularExpressions;

namespace SumStringAsNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.sumStrings("01", "2"));
        }
    }

    public static class Kata
    {
        public static string sumStrings(string a, string b)
        {
            //  No input checking. Assumes all chars are numerals.
            if (a.Length >= b.Length)
                b = String.Concat(new String('0', a.Length - b.Length), b);
            else
                a = String.Concat(new String('0', b.Length - a.Length), a);

            int carry = 0;
            string result = "";
            for (int i = a.Length - 1; i >= 0; i--)
                result = String.Concat(sumChars(a[i].ToString(), b[i].ToString(), ref carry), result);

            return Regex.Replace(String.Concat(carry.ToString(), result), @"^([0]*)(\d*)$", "$2");
        }

        public static string sumChars(string a, string b, ref int carry)
        {
            int sum = Int16.Parse(a) + Int16.Parse(b) + carry;
            carry = sum / 10;
            return (sum % 10).ToString();
        }
    }
}
