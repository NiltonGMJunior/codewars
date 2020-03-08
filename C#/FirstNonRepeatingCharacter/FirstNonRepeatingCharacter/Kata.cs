using System.Collections.Generic;

namespace FirstNonRepeatingCharacter
{
    public class Kata
    {
        public static string FirstNonRepeatingLetter(string s)
        {
            var allSet = new HashSet<string>();
            var duplicateSet = new HashSet<string>();
            foreach (var c in s)
            {
                if (allSet.Contains(c.ToString().ToLower()))
                    duplicateSet.Add(c.ToString().ToLower());
                allSet.Add(c.ToString().ToLower());
            }

            foreach (var c in s)
            {
                if (!duplicateSet.Contains(c.ToString().ToLower()))
                    return c.ToString();
            }
            return "";
        }
    }
}