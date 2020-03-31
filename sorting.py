
#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    #we need to compare the first index on the xs list,
    #with the first index on the ys list
    out=[]
    left_ix = 0
    right_ix = 0
    while left_ix<len(xs) and right_ix<len(ys):
        comparison=cmp(xs[left_ix],ys[right_ix])
        if comparison ==-1:
            out.append(xs[left_ix])
            left_ix=left_ix+1
        if comparison==1:
            out.append(ys[right_ix])
            right_ix=right_ix+1
        if comparison==0:
            out.append(xs[left_ix])
            out.append(ys[right_ix])
            left_ix=left_ix+1
            right_ix=right_ix+1
    while (left_ix < len(xs)) or (right_ix < len(y)):
        if left_ix < len(xs):
            out.append(xs[left_ix])
            left_ix=left_ix+1
        else:
            out.append(ys[right_ix])
            right_ix= right_ix+1
    return out 




def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:
        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves
    You should return a sorted version of the input list xs
    '''
    if len(xs) <=1:
        return xs
    else:
        middle=len(xs)//2
        left=xs[:middle]
        right=xs[middle+1:]
        left_sorted=merge_sorted(left,cmp)
        right_sorted=merge_sorted(right,cmp)
        return _merged(left_sorted,right_sorted,cmp)
        
        
def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.
    The pseudocode is:
        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)
    You should return a sorted version of the input list xs

    '''
    
  #if p<value  =-1- values are grather than 
  #if value<p  =1, equal=0 values are less than 
    if len(xs)<=1:
        return xs
    else:
        p=xs[0]
        less_than=[]
        greater_than=[]
        equal=[]
        for i in xs:
            comparison=cmp(p,xs[i])
            if comparison ==-1:
                greater_than.append(xs[i])
            if comparison ==1:
                less_than.append(xs[i])
            else:
                equal.append(xs[i])
                
        greater_sorted= quick_sorted(greater_than,cmp)
        less_sorted= quick_sorted(less_than,cmp)
        list_sorted= greater_sorted +less_sorted+equal
        return list_sorted 
            
        
def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.
    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
    if len(xs)<=1:
        return xs
    def quicksort(xs,lo, hi,cmp=cmp_standard):
        if lo<hi:
            p = partition(xs,lo,hi,cmp)
            quicksort(xs,lo,p-1,cmp)
            quicksort(xs,p+1,hi,cmp)
            return xs
    return quicksort(xs,0,len(xs)-1,cmp)

#from wiki:
#algorithm quicksort(A, lo, hi) is
    #if lo < hi then
        #p := partition(A, lo, hi)
        #quicksort(A, lo, p - 1)
        #quicksort(A, p + 1, hi)

#algorithm partition(A, lo, hi) is
    #pivot := A[hi]
    #i := lo
    #for j := lo to hi do
        #if A[j] < pivot then
            #swap A[i] with A[j] move forward
            #i := i + 1
    #swap A[i] with A[hi]
    #return i


def partition(xs,lo,hi,cmp=cmp_standard):
    pivot=xs[hi]
    i = lo
    #consider two cmp situations
    if cmp==cmp_standard:
        for j in range(lo,hi):
            if xs[j]<pivot:
                i=i+1
                xs[i]=xs[j]
                xs[j]=xs[i]
                #swap
        xs[i]=xs[hi]
        xs[hi]=xs[i]
        #because everytime we are comparing the new lo with the border
        
     #consider two cmp situations
    elif cmp==cmp_reverse:
        for j in range(lo,hi):
            if xs[j]>pivot:
                i=i+1
                xs[i]=xs[j]
                xs[j]=xs[i]
                #swap
        xs[i]=xs[hi]
        xs[hi]=xs[i]
    return i










    

