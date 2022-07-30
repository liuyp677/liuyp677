# 选择排序

def select_sort(li):
    length = len(li)
    for i in range(length - 1):
        min_loc = i
        for j in range(length - i):   #注意这里的范围必须是length-1，而不是length-1-i，会出错的！
            if li[i + j] < li[min_loc]:
                min_loc = i + j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]

li = [7,8,8,5,4,5,1,3,5,6,7,9,3,452,1]
select_sort(li)
print(li)
