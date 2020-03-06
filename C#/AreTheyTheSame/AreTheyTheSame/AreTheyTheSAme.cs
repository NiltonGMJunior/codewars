using System.Linq;

namespace AreTheyTheSame
{
    public class AreTheyTheSAme
    {
        public static bool comp(int[] a, int[] b)
        {
            if (a == null || b == null)
                return false;

            var listA = a.Select(i => i * i).ToList();
            var listB = b.ToList();

            listA.Sort();
            listB.Sort();

            if (Enumerable.SequenceEqual(listA, listB))
                return true;

            return false;
        }
    }
}