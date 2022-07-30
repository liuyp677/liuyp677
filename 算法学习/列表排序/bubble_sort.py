# 冒泡排序

def bubble_sort(li):
    length = len(li)
    for i in range(length - 1):
        exchange = False
        for j in range(length - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break

li = [7,8,8,5,4,5,1,3,5,6,7,9,3,452,1]
bubble_sort(li)
print(li)