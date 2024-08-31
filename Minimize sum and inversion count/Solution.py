def solution(N, A):
    maxi = A[0]
    sum = A[0]
    for i in range(1,N):
        if A[i]<A[i-1]:
            sum += A[i-1] * (n-i)
            break
        else:
            sum += A[i]
    return sum
