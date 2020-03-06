using System;

/*
 * Decode the Morse code - Codewars
 * Nilton Gomes Martins Junior
 * 04/03/2020
 * https://www.codewars.com/kata/54b724efac3d5402db00065e/train/csharp
 */
namespace DecodeTheMorseCode
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                var encodedMessage = Console.ReadLine();
                if (encodedMessage.Trim() == "")
                    break;
                Console.WriteLine(MorseCodeDecoder.Decode(encodedMessage));
            }
        }
    }
}
