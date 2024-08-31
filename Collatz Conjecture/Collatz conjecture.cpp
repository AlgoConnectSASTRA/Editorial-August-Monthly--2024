#include <iostream>
#include <vector>
using namespace std;

vector<int> solution(int n) {
    /*
        This function generates the sequence for the Collatz Conjecture starting with a given integer n.
        
        Approach:
            1. Initialize an empty vector `output` to store the sequence.
            2. Continue looping until n becomes 1:
                - Append the current value of n to the vector `output`.
                - If n is even, update n to n / 2.
                - If n is odd, update n to 3 * n + 1.
            3. After the loop, append 1 to the `output` vector.
            4. Return the sequence vector.
    */

    vector<int> output;
    while (n != 1) {
        output.push_back(n);
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    output.push_back(1);  // Append 1 when n becomes 1
    
    return output;
}

