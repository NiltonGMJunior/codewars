/*
 * Write Number in Expanded Form - Codewars
 * Nilton Gomes Martins Junior
 * 08/03/2020
 * https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/csharp
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace WriteNumberInExpandedForm
{
    public static class Kata
    {
        public static string ExpandedForm(long num)
        {
            //  Assumes that all numbers will be whole numbers greater than 0.
            long div = 10;
            var parcels = new List<long>();
            do
            {
                parcels.Add(num % div);
                num -= num % div;
                div *= 10;
            } while (num / div != 0);
            parcels.Add(num);

            return String.Join(" + ", parcels.Where(p => p != 0).Reverse());
        }
    }
}