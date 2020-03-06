namespace IsThisATriangle
{
    public class Triangle
    {
        public static bool IsTriangle(int a, int b, int c)
        {
            if (a >= b + c || b >= a + c || c >= a + b)
                return false;
            return true;
        }
    }
}