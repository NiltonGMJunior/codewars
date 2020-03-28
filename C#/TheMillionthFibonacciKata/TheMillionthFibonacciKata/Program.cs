/*
 * The Millionth Fibonacci Kata - Codewars
 * Nilton Gomes Martins Junior
 * 28/03/2020
 * https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/csharp
 */

using System;
using System.Numerics;

namespace TheMillionthFibonacciKata
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Fibonacci.fib(100));
        }
    }


    public class Fibonacci
    {
        // TODO: Improve code efficiency. Running times are greater than the timeout interval.
        public static BigInteger fib(int n)
        {
            if (n == 0)
                return 0;

            if (n > 0)
            {
                var fibSeq = new BigInteger[n + 1];
                fibSeq[0] = 0;
                fibSeq[1] = 1;
                for (int i = 2; i < n + 1; i++)
                    fibSeq[i] = fibSeq[i - 1] + fibSeq[i - 2];
                return fibSeq[n];
            }
            else
            {
                var fibSeq = new BigInteger[-n + 2];
                fibSeq[-n + 1] = 1;
                fibSeq[-n] = 0;
                for (int i = -n - 1; i >= 0; i--)
                    fibSeq[i] = fibSeq[i + 2] - fibSeq[i + 1];
                return fibSeq[0];
            }
        }
    }
}
