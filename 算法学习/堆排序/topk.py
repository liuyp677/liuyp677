# 利用堆排序原理，获得最大的K个值

# 大根堆sift
# def sift(li, low, high):
#     tmp = li[low]
#     i = low # 父节点
#     j = low * 2 + 1 # 左节点
#     while j <= high:# 当左节点存在时
#         if j + 1 <= high and li[j + 1] > li[j]:# 当右节点存在时，选出较大节点，并实现较大叶子节点上移
#             j = j + 1
#         if tmp < li[j]:
#             li[i] = li[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             li[i] = tmp
#             break
#     else:
#         li[i] = tmp


# 小根堆sift
def sift(li, low, high):
    tmp = li[low]
    i = low
    j = low * 2 + 1  # 叶子左节点
    while j <= high:
        if j + 1 <= high and li[j] > li[j + 1]:
            j = j + 1
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = i * 2 + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk_sort(li, k):
    n = len(li)
    la = li[0:k]
    for i in range((k-2)//2, -1, -1): # 形成小根堆
        sift(la, i, k-1)
    for i in range(k, n): # 
        if li[i] > la[0]:
            la[0], li[i] = li[i], la[0]
            sift(la, 0 , k-1)
    for i in range(k-1, -1,-1):
        la[0], la[i] = la[i], la[0]
        sift(la, 0, i-1)
    print(la)





li = list(i for i in range(100))
import random
random.shuffle(li)
print(li)

topk_sort(li, 10)



# 现在有N个数，设计算法得到前K大的数（K<N)
# 解决思路：
# 1、排序后切片 O(nlogn)---快速排序
# 2、排序三人组 O(kn)---冒泡、排序、选择排序
# 3、堆排序思路 O(nlogk)---对堆取前面K值建立小根堆，堆顶就是最小的值，对后续n-k个值分别比较与第一个值的大小，大于则成为堆顶【必须是小根堆】