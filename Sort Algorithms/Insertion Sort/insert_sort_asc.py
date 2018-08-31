'''插入排序，升序'''

def insert_sort(L):
    n = len(L)
    if n == 1:
        return

    # 首先，假设第1个元素L[0]是 "已排序序列"，第2个元素L[1]至最后一个元素L[n-1]是 "未排序序列"
    for i in range(1, n):  # 共需要 n-1 次插入操作。 i 表示 "未排序序列" 的第1个元素的下标，所以 i 从下标 1 开始

        # j 的范围是 [i, i-1，... 2, 1]，即包含下标 i 和 "已排序序列" 的所有下标
        for j in range(i, 0, -1):  # 将 "未排序序列" 的第1个元素L[i]，依次与 "已排序序列" 中的所有元素比较
            if L[j] < L[j-1]:  # 如果小于前一个元素，则交换位置
                L[j], L[j-1] = L[j-1], L[j]
            else:  # 如果不小于前一个元素，则肯定不小于这个元素之前的所有元素（因为前面已排好序了），所以可以退出比较的循环
                break


def insert_sort2(L):
    n = len(L)
    if n == 1:
        return

    for i in range(1, n):
        '''
        第3次插入的过程：

        i = 3，此时列表为 [26, 54, 93, 17, 77, 31, 44, 55, 20]，"已排序序列" 为[26, 54, 93]，"未排序序列" 为[17, 77, 31, 44, 55, 20]
        temp = L[3]  # 17

        j = i - 1  # 2
        此时，while条件为True，L[j+1] = L[j]，即L[3] = L[2] = 93，会覆盖之前的17，所以temp变量的作用就是先保留该值
        列表变为 [26, 54, 93, 93, 77, 31, 44, 55, 20]

        j -= 1  # 1
        此时，while条件为True，L[j+1] = L[j]，即L[2] = L[1] = 54
        列表变为 [26, 54, 54, 93, 77, 31, 44, 55, 20]

        j -= 1  # 0
        此时，while条件为True，L[j+1] = L[j]，即L[1] = L[0] = 26
        列表变为 [26, 26, 54, 93, 77, 31, 44, 55, 20]

        j -= 1  # -1
        此时，while条件为False，L[j+1] = temp，即L[0] = temp = 17
        列表变为 [17, 26, 54, 93, 77, 31, 44, 55, 20]
        至此，已将 "未排序序列" [17, 77, 31, 44, 55, 20] 的第1个元素17插入到 "已排序序列" [26, 54, 93] 的正确位置
        '''
        temp = L[i]  # "未排序序列" 的第1个元素
        j = i - 1  # "已排序序列" 的最后1个元素，因为要从后向前比较 "已排序序列"
        while j >= 0 and temp < L[j]:  # 如果 "未排序序列" 的第1个元素，小于 "已排序序列" 中的元素L[j] (j>=0表示没有超出 "未排序序列" 的下标范围)
            L[j+1] = L[j]  # 则将 "已排序序列" 中的元素L[j]的值复制给L[j+1]，相当于L[j]向后挪了一个位置
            j -= 1
        # 如果while条件为False：
        # 1. j < 0，则将 "未排序序列" 的第1个元素赋值给L[0]
        # 2. temp >= L[j]，则将 "未排序序列" 的第1个元素 "插入" 到L[j]的后面（自己尝试 i=4 时，就知道了）
        L[j+1] = temp


L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('Before: ', L1)
insert_sort(L1)
print('After: ', L1)

# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]