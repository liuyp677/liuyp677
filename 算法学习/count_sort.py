# 计数排序 限定数字范围0-N，一种时间复杂度在O(n)的算法

def count_sort(li, n):
    la = [0 for _ in range(n + 1)]
    for i in li:
        la[i] += 1
    li.clear()
    for ind, val in enumerate(la):
        for i in range(val):
            li.append(ind)
    
import random
li = [random.randint(0, 100) for _ in range(300)]
print(li)
count_sort(li, 100) 
print(li)