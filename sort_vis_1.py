import random
import time
from graphics import graphics

def selection_sort(l):
    begin = 0
    for i in range(0, len(l)):
        small_i = begin
        for j in range(begin, len(l)):
            if l[small_i] > l[j]:
                small_i = j
        l[begin], l[small_i] = l[small_i], l[begin]
        begin += 1
    return l

def bubble_sort(l):
    end = len(l)
    for i in range(0, len(l)):
        for j in range(0, end-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        end -= 1
    return l
    
def insertion_sort(l):
    for compare_index in range(1, len(l)):
        ci = compare_index
        for j in range(ci-1, -1, -1):
            if ci < 0 or l[ci] >= l[j]:
                break
            else:
                l[ci], l[j] = l[j], l[ci]
                ci -= 1
    return l

def get_random_list(length):
    l = []
    for i in range(length):
        r = random.randint(0, length)
        l.append(r)
    return l

def main():
    
    height = 400
    width = 700
    gui = graphics(width, height, 'vis')
    
main()