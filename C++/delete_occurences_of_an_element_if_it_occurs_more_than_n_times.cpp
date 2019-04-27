/*  Delete occurrences of an element if it occurs more than n times   -   CodeWars
    Nilton Gomes Martins Junior
    14/04/2019
    https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/cpp
*/

#include <vector>

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
    // Naive solution attempt
    std::vector<int> output;
    for (unsigned int iii = 0; iii < arr.size(); ++iii)
    {
        unsigned int count = 0;
        for (unsigned int jjj = 0; jjj < output.size(); ++jjj)
        {
            if (output[jjj] == arr[iii]) count++;
        }
        if (count < n) output.push_back(arr[iii]);
    }

    return output;
}

int main()
{

    return 0;
}

