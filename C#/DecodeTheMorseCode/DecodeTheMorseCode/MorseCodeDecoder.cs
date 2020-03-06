using System;
using System.Collections.Generic;
using System.Text;

namespace DecodeTheMorseCode
{
    class MorseCodeDecoder
    {
        public static string Decode(string morseCode)
        {
            var decodedMessage = new StringBuilder();
            var strippedMessage = morseCode.Trim();
            var words = strippedMessage.Split("   ");
            foreach (var word in words)
            {
                var chars = word.Split(" ");
                foreach (var c in chars)
                {
                    decodedMessage.Append(MorseCode.Get(c));
                }

                decodedMessage.Append(" ");
            }

            return decodedMessage.ToString().Trim();
        }
    }
}
