/*
 * Are they the "same"? - Codewars
 * Nilton Gomes Martins Junior
 * 03/03/2020
 * https://www.codewars.com/kata/550498447451fbbd7600041c/train/csharp
 */
using System;
using System.Linq;

namespace AreTheyTheSame
{
    class Program
    {
        static void Main(string[] args)
        {
            //int[] a = new int[] { 121, 144, 19, 161, 19, 144, 19, 11 };
            //int[] b = new int[] { 121, 14641, 20736, 361, 25921, 361, 20736, 361 };

            int[] a = new int[] {};
            int[] b = new int[] {};

            Console.WriteLine(AreTheyTheSAme.comp(a, b));
        }
    }
}
