/*
 * Create Phone Number
 * Nilton Gomes Martins Junior
 * 08/03/2020
 * https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/csharp
 */

using System;
using System.Text.RegularExpressions;

namespace CreatePhoneNumber
{
    public class Kata
    {
        public static string CreatePhoneNumber(int[] numbers)
        {
            var numString = String.Join("", numbers);
            return Regex.Replace(numString, @"(\d{3})(\d{3})(\d{4})", @"($1) $2-$3");
        }
    }
}