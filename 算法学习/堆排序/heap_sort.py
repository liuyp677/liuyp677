# 堆排序，不需使用递归

# 首先实现一个向下调整的基本结构
def sift(li, low, high):
    tmp = li[low]
    i = low # 父节点
    j = low * 2 + 1 # 左节点
    while j <= high:# 当左节点存在时
        if j + 1 <= high and li[j + 1] > li[j]:# 当右节点存在时，选出较大节点，并实现较大叶子节点上移
            j = j + 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


# 实现堆排序，从下往上逐步进行向下调整
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1): # 建堆过程，建立大根堆
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):  # 排序过程
        li[0], li[i] = li[i], li[0] # 根节点肯定最大，取列表最后一位替换，最后形成从小到大排序的列表
        sift(li, 0, i - 1)



li = list(i for i in range(100))
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)