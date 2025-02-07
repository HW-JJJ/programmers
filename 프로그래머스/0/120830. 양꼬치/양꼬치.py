def solution(n, k):
    
    for i in range(100):
        if (10 * i) <= n < (10 * (i+1)) :
            answer =  12000 * n + 2000 * k - 2000 * i
    return answer