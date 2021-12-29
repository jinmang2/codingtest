```python
def solution(citations):
    for h in range(max(citations), 0, -1):
        if sum([True for i in citations if i >= h]) >= h:
            return h
        
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
```
