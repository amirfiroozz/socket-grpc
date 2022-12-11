from abc import ABC , abstractclassmethod
import server.helper as helper
import time

class Sort(ABC):
    @abstractclassmethod
    def sort(self):
        """interface for all sorting algorithms"""

class InsertionSort(Sort):
    def sort(self , arr , sleepTime):
        err = helper.generateNoErrorGRPCResponse()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    j -= 1
                    yield from helper.setSortingResponseArray(arr , False , err)
                    time.sleep(sleepTime)
            arr[j+1] = key
        yield from helper.setSortingResponseArray(arr , True , err)

class BubbleSort(Sort):
    def sort(self , arr , sleepTime):
        err = helper.generateNoErrorGRPCResponse()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield from helper.setSortingResponseArray(arr , False , err , j , j+1)
                    time.sleep(sleepTime)
        yield from helper.setSortingResponseArray(arr , True , err)

class SelectionSort(Sort):
    def sort(self , arr , sleepTime):
        err = helper.generateNoErrorGRPCResponse()
        size = len(arr)
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[ind], arr[min_index] = arr[min_index], arr[ind]
            yield from helper.setSortingResponseArray(arr , False , err , ind ,min_index )
            time.sleep(sleepTime)
        yield from helper.setSortingResponseArray(arr , True , err)

class MergeSort(Sort):
    def sort(self , arr , sleepTime):
        err = helper.generateNoErrorGRPCResponse()
        width = 1   
        n = len(arr)                                         
        while (width < n):
            l=0
            while (l < n):
                r = min(l+(width*2-1), n-1)        
                m = min(l+width-1,n-1)
                self.merge(arr, l, m, r)
                yield from helper.setSortingResponseArray(arr , False , err)
                time.sleep(sleepTime)
                l += width*2
            width *= 2
        yield from helper.setSortingResponseArray(arr , True , err)
    
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = arr[l + i]
        for i in range(0, n2):
            R[i] = arr[m + i + 1]
    
        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

class QuickSort(Sort):
    def sort(self , arr , sleepTime):
        err = helper.generateNoErrorGRPCResponse()
        l , h = 0 , len(arr)-1
        size = h - l + 1
        stack = [0] * (size)
        top = -1
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h
        while top >= 0:
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1
            p , right = self.partition( arr, l, h )
            yield from helper.setSortingResponseArray(arr , False , err , p , right)
            time.sleep(sleepTime)
            if p-1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1
            if p+1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
        yield from helper.setSortingResponseArray(arr , True , err)
        
    def partition(self,arr,l,h):
        i = ( l - 1 )
        x = arr[h]
        for j in range(l , h):
            if   arr[j] <= x:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[h] = arr[h],arr[i+1]
        return (i+1, h)


def sortingFactory(t):
    if t=="insertion":
        return InsertionSort()
    elif t=="bubble":
        return BubbleSort()
    elif t=="selection":
        return SelectionSort()
    elif t=="merge":
        return MergeSort()
    elif t=="quick":
        return QuickSort()
    else:
        return InsertionSort()

