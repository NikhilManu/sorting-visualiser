def merge_sort(arr, lb, ub):
    if ub <= lb:
        return
    elif lb < ub:
        mid = (lb+ub)//2
        yield from merge_sort(arr, lb, mid)
        yield from merge_sort(arr, mid+1, ub)
        yield from merge(arr, lb, mid, ub)
        yield arr


def merge(arr, lb, mid, ub):
    new = []
    i = lb
    j = mid+1
    while i <= mid and j <= ub:
        if arr[i] < arr[j]:
            new.append(arr[i])
            i += 1
        else:
            new.append(arr[j])
            j += 1
    if i > mid:
        while j <= ub:
            new.append(arr[j])
            j += 1
    else:
        while i <= mid:
            new.append(arr[i])
            i += 1
    for i, val in enumerate(new):
        arr[lb+i] = val
        yield arr

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]


def quicksort(A, start, end):

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


def insertionsort(A):

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A