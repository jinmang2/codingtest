"""
# Initial points

Rotate 0
--------
:math: $$a_{0,\,loop}^{0}=\sum_{k=1}^{loop}{\big(n-k\big)}$$

Rotate 1
--------
:math: $$a_{0,\,loop}^{1}=loop-\bigg(1+\sum_{k=1}^{2 * loop}{k}\bigg)$$

Rotate 2
--------
:math: $$a_{0,\,loop}^{2}=1+\sum_{k=2}^{loop}{\big(n-k+2\big)}$$
"""

TestCase = {
    1: [1],
    2: [3,1,2],
    3: [5,6,1,4,2,3],
    4: [7,8,9,1,6,10,2,5,3,4],
    5: [9,10,11,12,1,8,15,13,2,7,14,3,6,4,5],
    6: [11,12,13,14,15,1,10,20,21,16,2,9,19,17,3,8,18,4,7,5,6],
    7: [13,14,15,16,17,18,1,12,25,26,27,19,2,11,24,28,20,3,10,23,21,4,9,22,5,8,6,7]
}


def solution(n):
    cnt = 0
    answer = [0] * int(n * (n + 1) / 2)
    for i in range(n):
        rotate = i % 3
        loop = i // 3 + 1
        # initial setting
        if rotate == 0:
            ind = sum(n - k - 1 for k in range(loop))
        elif rotate == 1:
            ind = loop - (sum(k+1 for k in range(2*loop)) + 1)
        else:
            ind = 1 + sum(n - k + 1 for k in range(loop-1))
        for j in range(n-i):
            cnt += 1
            answer[ind] = cnt
            if rotate == 0:
                ind += n - j - loop
            elif rotate == 1:
                ind -= j + 3 + (loop - 1) * 2
            else:
                ind += 1
    return answer
  
  
 if __name__ == "__main__":
      n = 7
      print(solution(n))
      print(TestCase(n))
