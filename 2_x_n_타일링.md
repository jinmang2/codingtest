## 문제 설명
가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우
예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

<p align="center">
  <img src=https://i.imgur.com/29ANX0f.png>
</p>


직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

**제한사항**
- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

## 문제 풀이
```python
def solution(n):
    res = 0
    if n in [1, 2]:
        return n
    a = 1; b = 2
    for i in range(3, n+1):
        res = (a + b) % 1000000007
        a = b
        b = res
    return res
    # if (n == 1) | (n == 2):
    #     return n % 1000000007
    # else:
    #     return solution(n-1) + solution(n-2)
    
# n=1 >> 1
# n=2 >> 11, =
# n=3 >> 111, 1=, =1
# n=4 >> 1111, 11=, 1=1, =11
# n=5 >> 11111, 111=, 11=1, 1=11, =111, 1==, =1=, ==1
# n=6 >> 111111, 1111=, 111=1, 11=11, 1=111, =1111, 11==, 1=1=, =11=, 1==1, =1=1, ==11, ===

# 1, 2, 3, 5, 8, 13, ...
# fibonacci sequence
# F(n) = F(n-1) + F(n-2)


# def solution(n):
#     a = 1
#     res = 2
#     if (n == 1) | (n == 2):
#         return n
#     for i in range(3, n+1):
#         res += a % 1000000007
#         a = (res - a) % 1000000007
#     return res

def solution(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1000000007
```
