#include <iostream>
using namespace std;

string solution(int a, int b) {
    /*
        The function determines if it's possible to make both heaps empty by performing the following operations:
        - Remove 2 from heap A and 1 from heap B
        - Or remove 1 from heap A and 2 from heap B

        Approach:
        1. Continue to perform operations based on the larger heap:
           - If heap A is larger, remove 2 from A and 1 from B.
           - If heap B is larger or equal, remove 2 from B and 1 from A.
        2. Stop when at least one heap is empty.
        3. If both heaps are empty, return "YES"; otherwise, return "NO".
    */
    
    while (a > 0 && b > 0) {
        if (a > b) {
            a -= 2;
            b -= 1;
        } else {
            b -= 2;
            a -= 1;
        }
    }
    
    return (a == 0 && b == 0) ? "YES" : "NO";
}
