/*  Vowel Count   -   CodeWars
    Nilton Gomes Martins Junior
    09/05/2019
    https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/cpp
*/

#include <iostream>
#include <string>

int getCount(const std::string& inputStr)
{
    int num_vowels = 0;

    for (auto& ch : inputStr)
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            num_vowels++;

    return num_vowels;
}

int main()
{

    return 0;
}