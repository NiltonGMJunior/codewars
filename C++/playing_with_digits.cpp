/*  Playing with digits   -   CodeWars
    Nilton Gomes Martins Junior
    10/05/2019
    https://www.codewars.com/kata/playing-with-digits/train/cpp
*/

#include <iostream>
#include <cmath>
#include <string>

class DigPow
{
    public:

    static int digPow(int n, int p)
    {
        int sum = 0;
        for (auto& ch : std::to_string(n))
            sum += static_cast<int>(pow(ch - '0', p++));
        
        int result = -1;
        if (sum / n - static_cast<double>(sum)/n == 0)
            result = sum / n;
        return result;
    }
};

int main(int argc, char const *argv[])
{
    DigPow digpow;
    int result = digpow.digPow(46288, 3);
    std::cout << result << "\n";
    return 0;
}

