/*
 * Bagels - Codewars
 * Nilton Gomes Martins Junior
 * 30/03/2020
 * https://www.codewars.com/kata/54bd6b4c956834c9870001a1/train/csharp
 */

using System;

namespace Bagels
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }

    public class BagelSolver
    {
        public static Bagel Bagel
        {
            get
            {
                Bagel bagel = new Bagel();
                bagel.GetType().GetProperty("Value").SetValue(bagel, 4);
                return bagel;
            }
        }
    }

    public sealed class Bagel
    {
        public int Value { get; private set; } = 3;
    }
}
