# 希尔排序 可以理解为分组插入排序

def insert_sort_gap(li, gap):  # 基于间隔的插入排序
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j = j - gap
        li[j + gap] = tmp

def shell_sort(li):  #实现分组
    gap = len(li) // 2
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap = gap // 2
    print(li)

li = [i for i in range(1000)]
import random
random.shuffle(li)
shell_sort(li)


