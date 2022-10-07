#!/usr/bin/python
# -*- coding:utf-8 -*-


print('<<<<<<<<<<<<<<<<<<链表反转>>>>>>>>>>>>>>>>>>>>>>')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 1->2->3->4->5  转成 1<-2<-3<-4<-5
    def reverse_list(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


print('<<<<<<<<<<<<<<<<<<<<<<<二分法查找>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 思路，递归找到中间值，然后比较当前查找值跟中间值的大小
def half_search(sorted_list, x):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if x > sorted_list[mid]:
            low = mid + 1
        elif x < sorted_list[mid]:
            high = mid - 1
        else:
            return mid, sorted_list[mid]
    return 'no'


nums = [6, 13, 21, 43, 55]
target = 13
print(half_search(nums, target))

print('<<<<<<<<<<<<<<<<<<<<快速排序>>>>>>>>>>>>>>>>>>>>>>')


# 快速排序
def partition(li, left, right):
    """
    每次排序，取第一个元素充当tmp,此时列表空出第一个元素的位置，然后先从右边找出比tmp小的数，填充到空缺位置，再从左到右查找
    比tmp大的数填充到空缺位置
    : 排序的结果是列表的第一个元素找到了它应该呆的位置，同时将小于该元素的元素移到了左边，大于该元素的元素移到了右边
    """
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 继续从右往左查找
        li[left] = li[right]  # 把右边的值写到左边空位上

        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上

    li[left] = tmp  # 把tmp归位
    return left


def quick_sort(li, left, right):
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


_li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(_li, 0, len(_li) - 1)
print(_li)

print('<<<<<<<<<<<<<<<<<<<堆排序>>>>>>>>>>>>>>>>>>')


# 先转换成大顶堆
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)

print('<<<<<<<<<<<<<<<<<<<冒泡排序>>>>>>>>>>>>>>>>>')


def bubble_sort(arr):
    """
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
    两两比较
    """
    # 遍历所有数组元素
    for i in range(len(arr)):
        # Last i elements are already in place
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print(arr)

print('<<<<<<<<<<<<<<<<<<<选择排序>>>>>>>>>>>>>>>>>>>>>')


def select_sort(_list):
    """
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    """
    for i in range(len(_list)):
        max_idx = i
        for j in range(i + 1, len(_list)):
            if _list[j] > _list[max_idx]:
                max_idx = j
        _list[i], _list[max_idx] = _list[max_idx], _list[i]
    return _list


A = [64, 25, 12, 22, 11]
res = select_sort(A)
print(res)

print('<<<<<<<<<<<<<<<<<<<<<<二分查找{输出有序列表中绝对值最小的元素}>>>>>>>>>>>>>>>>>>>>>>>>')


def mid_search(arr):
    if not arr:
        return
    if len(arr) == 1:
        return arr[0]
    mid_index = len(arr) // 2
    mid = arr[mid_index]
    left = arr[mid_index - 1]
    if abs(mid) < abs(left):
        arr = arr[mid_index:]
    else:
        arr = arr[:mid_index]
    return mid_search(arr)


b = [-1, 0, 1, 2, 3]
a = mid_search(b)
print(a)
