/*  Find the next perfect square!   -   CodeWars
    Nilton Gomes Martins Junior
    14/04/2019
    https://www.codewars.com/kata/find-the-next-perfect-square/train/cpp
*/

#include <math.h>

long int findNextSquare(long int sq)
{
    unsigned long int root = pow(sq, 0.5);
    if (pow(root, 2) != sq) return -1; 
    return (root + 1) * (root + 1); 
}

int main()
{
    return 0;
}

