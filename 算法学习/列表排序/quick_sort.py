# 快速排序


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid)
        quick_sort(li, mid + 1, right)

li = [7,8,8,5,4,5,1,3,5,6,7,9,3,452,1]
quick_sort(li, 0, len(li) - 1)
print(li)