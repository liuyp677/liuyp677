# 归并排序，快速排序第三种，时间复杂度为O(nlogn)，空间复杂度为n

# 假设现在的列表为两段同样长度的有序序列，如何将其一次合并
def merge(li, low, mid, high):
    i = low 
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low : high + 1] = tmp



# 将列表变成两个有序列表，利用递归拆分
def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


# 实例
li = [1,2,6,7,5,8,9,12,4,3]
merge_sort(li, 0, len(li) - 1)
print(li)