/*  Playing with passphrases   -   CodeWars
    Nilton Gomes Martins Junior
    04/05/2018
    https://www.codewars.com/kata/559536379512a64472000053/train/c
*/

#include <stdio.h>
#include <stdlib.h>

char *playPass(char *s, int n)
{
    unsigned int length = 0;
    while (s[length++] != '\0');

    char *cypher = malloc(sizeof(char) * length);
    for (unsigned int iii = 0; iii < length - 1; ++iii)
    {
        if (s[length - 2 - iii] >= 'A' && s[length - 2 - iii] <= 'Z')
        {
            cypher[iii] = 'A' + (s[length - 2 - iii] + n - 'A') % ('Z' - 'A' + 1);
            if ((length - 2 - iii) % 2 != 0)
                cypher[iii] = 'a' + cypher[iii] - 'A';
        }
        else if (s[length - 2 - iii] >= '0' && s[length - 2 - iii] <= '9')
            cypher[iii] = '0' + '9' - s[length - 2 - iii];
        else
            cypher[iii] = s[length - 2 - iii];
    }

    return cypher;
}

int main()
{
    char *test = playPass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2);
    printf("%s\n", test);
    return 0;
}