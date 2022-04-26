import numpy as np
import time
from random import randint


def insertionSort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i-1
        while arr[j] > x and j > -1:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x


def selectionSort(arr, n):
    for i in range(0, n-1):
        k = i
        for j in range(i+1, n):
            if arr[j] < arr[k]:
                k = j
        if i != k:
            arr[i], arr[k] = arr[k], arr[i]


def bubbleSort(arr, n):
    for i in range(0, n-1):
        flag = 0
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break


def merge(arr, left, mid, right):
    nL = mid - left + 1
    nR = right - mid
    l = [0] * (nL)
    r = [0] * (nR)
    for i in range(0, nL):
        l[i] = arr[left + i]
    for j in range(0, nR):
        r[j] = arr[mid + 1 + j]
    i = j = 0
    k = left
    while i < nL and j < nR:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
            k += 1
        else:
            arr[k] = r[j]
            j += 1
            k += 1
    while i < nL:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < nR:
        arr[k] = r[j]
        j += 1
        k += 1


def mergeSort(arr, first, last):
    if first < last:
        mid = first+(last-first)//2
        mergeSort(arr, first, mid)
        mergeSort(arr, mid+1, last)
        merge(arr, first, mid, last)


def hybridMergeSelection(arr, first, last, threshold):
    length = last - first + 1
    if length <= threshold:
        selectionSort(arr, len(arr))
    elif first < last:
        mid = first+(last-first)//2
        hybridMergeSelection(arr, first, mid, threshold)
        hybridMergeSelection(arr, mid+1, last, threshold)
        merge(arr, first, mid, last)


def randomizedPartition(arr, p, r):
    pivotid = randint(p, r)
    x = arr[pivotid]
    arr[pivotid], arr[r] = arr[r], arr[pivotid]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def findk(arr, low, high, k):
    q = randomizedPartition(arr, low, high)
    if q == k-1:
        return arr[q]
    elif q < k-1:
        return findk(arr, q+1, high, k)
    else:
        return findk(arr, low, q-1, k)


def quickSort(arr, p, r):
    if p < r:
        q = randomizedPartition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


def arrayGenerator():
    low = int(input("please enter the lowest possible number in random array: "))
    high = int(input("please enter the highest possible number in random array: "))
    size = int(input("please enter the size of the random array: "))
    return np.random.randint(low, high+1, size)


def sort(arr):
    run = True
    length = len(arr)
    while(run):
        print("Please choose a sorting technique:")
        choice = input(
            "1. Insertion sort\n2. Selection sort\n3. Merge sort\n4. Quick sort\n5. Hybrid merge selection sort\n6. Find kth smallest element\n7. Exit\n")
        if choice == "1":
            a = arr.copy()
            print("Original array: ")
            print(a)
            start = time.perf_counter()*1000
            insertionSort(a)
            end = time.perf_counter()*1000
            print("Sorted array: ")
            print(a)
            print("Running time for insertion sort is " +
                  str(end - start) + " ms")
        elif choice == "2":
            b = arr.copy()
            print("Original array: ")
            print(b)
            start = time.perf_counter()*1000
            selectionSort(b, length)
            end = time.perf_counter()*1000
            print("Sorted array: ")
            print(b)
            print("Running time for selection sort is " +
                  str(end - start) + " ms")
        elif choice == "3":
            c = arr.copy()
            print("Original array: ")
            print(c)
            start = time.perf_counter()*1000
            mergeSort(c, 0, length-1)
            end = time.perf_counter()*1000
            print("Sorted array: ")
            print(c)
            print("Running time for merge sort is " + str(end - start) + " ms")
        elif choice == "4":
            d = arr.copy()
            print("Original array: ")
            print(d)
            start = time.perf_counter()*1000
            quickSort(d, 0, length-1)
            end = time.perf_counter()*1000
            print("Sorted array: ")
            print(d)
            print("Running time for quick sort is " + str(end - start) + " ms")
        elif choice == "5":
            e = arr.copy()
            print("Original array: ")
            print(e)
            threshold = int(input("Enter threshold value: "))
            start = time.perf_counter()*1000
            hybridMergeSelection(e, 0, length-1, threshold)
            end = time.perf_counter()*1000
            print("Sorted array: ")
            print(e)
            print("Running time for hybrid merge sort is " +
                  str(end - start) + " ms")
        elif choice == "6":
            f = arrayGenerator()
            print("Original array: ")
            print(f)
            k = input("to find kth smallest element, enter a value for k: ")
            num = findk(f, 0, length-1, int(k))
            print("The value of the %d smallest element is: " % int(k))
            print(num)
        elif choice == "7":
            run = False
        else:
            print("INVALID CHOICE, please try again!")
            time.sleep(1)


arr = arrayGenerator()
sort(arr)
