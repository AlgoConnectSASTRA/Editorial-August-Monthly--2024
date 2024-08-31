#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n, const vector<int>& heights) {
    /*
        Approach:
            1. Initialize `maximum` with the height of the first step to keep track of the highest step seen so far.
            2. Initialize `result` to 0, which will accumulate the total amount of "increased height" needed.
            3. Iterate through the heights vector:
                - Update `maximum` to be the maximum of the current `maximum` and the current step height.
                - If the current step height is less than the `maximum`, add the difference (`maximum - heights[i]`) to `result`.
            4. Return the `result`, which represents the total height increases needed to make the heights non-decreasing.
    */

    int maximum = heights[0];
    int result = 0;

    for (int i = 0; i < n; ++i) {
        maximum = max(maximum, heights[i]);
        if (heights[i] < maximum) {
            result += (maximum - heights[i]);
        }
    }

    return result;
}
