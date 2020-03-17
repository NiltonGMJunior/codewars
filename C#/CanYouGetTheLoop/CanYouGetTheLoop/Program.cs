/*
 * Can you get the loop? - Codewars
 * Nilton Gomes Martins Junior
 * 15/03/2020
 * https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/csharp
 */
using System;
using System.Collections.Generic;

namespace CanYouGetTheLoop
{
    class Program
    {
        static void Main(string[] args)
        {
            var n1 = new LoopDetector.Node();
            var n2 = new LoopDetector.Node();
            var n3 = new LoopDetector.Node();
            var n4 = new LoopDetector.Node();
            n1.next = n2;
            n2.next = n3;
            n3.next = n4;
            n4.next = n2;

            Console.WriteLine(Kata.getLoopSize(n1));
        }
    }

    public class Kata
    {
        public static int getLoopSize(LoopDetector.Node startNode)
        {
            var nodeDict = new Dictionary<LoopDetector.Node, int>();
            LoopDetector.Node currentNode = startNode;
            int stepCounter = -1;
            while (!nodeDict.ContainsKey(currentNode))
            {
                nodeDict.Add(currentNode, ++stepCounter);
                currentNode = currentNode.next;
            }

            return stepCounter - nodeDict[currentNode] + 1;
        }
    }
}

namespace LoopDetector
{
    public class Node
    {
        public Node next { get; set; }
    }
}
