/*  Who likes it?   -   CodeWars
    Nilton Gomes Martins Junior
    14/04/2019
    https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/cpp
*/

#include <string>
#include <vector>
#include <iostream>

std::string likes(const std::vector<std::string> &names)
{
    unsigned int names_quant = names.size();
    switch (names_quant)
    {
        case 0: return "no one likes this";
        case 1: return names[0] + " likes this";
        case 2: return names[0] + " and " + names[1] + " like this";
        case 3: return names[0] + ", " + names[1] + " and " + names[2] + " like this";
        default: return names[0] + ", " + names[1] + " and " + std::to_string(names_quant - 2) + " others like this";
    }
}

int main()
{
    std::vector<std::string> test { "Peter" };
    std::cout << likes(test) << "\n";
    return 0;
}

