# 插入排序

def insert_sort(li):
    for i in range(len(li) - 1):
        j = i + 1
        tmp = li[j]
        while li[j - 1] > tmp and j > 0:        
            li[j] = li[j - 1]
            j -= 1     
        li[j] = tmp

li = [7,8,8,5,4,5,1,3,5,6,7,9,3,452,1]
insert_sort(li)
print(li)
