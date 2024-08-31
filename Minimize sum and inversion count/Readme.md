### Explanation:

[Problem link](www.hackerrank.com/contests/azac-august24/challenges/minimize-sum-and-inversion-count)

1. We can see that the array needs to be in non-decreasing order to have the minimum inversions (0)
2. Consider the following array {... x, y....}

   i. Where till x the array is non decreasing

   ii. x,y is an inversion pair

4. To make x,y non decreasing, **our only option** is to switch all elements from y till end, to x. via the given operation.
5. This makes the entire array non decreasing.
6. Hence the answer will be sum till index(x), and then x*(n-index(x))
