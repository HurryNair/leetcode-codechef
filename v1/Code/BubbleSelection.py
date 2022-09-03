import unittest

def bubbleSort(l):
    for i in range(0, len(l)):
        for j in range(1, len(l)-i):
            if l[j] < l[j-1]:
                swap(j-1, j, l)
    
    return l

def swap(i, j, l):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

print(bubbleSort([3, 21, 4, 5, 65]))

def selectionSort(l):
    max = 0
    for i in range(0, len(l)):
        for j in range(1, len(l)-i):
            if l[j] > max:
                max = j
        swap(max, len(l)-1-i, l)
    
    return l

print(selectionSort([3, 21, 4, 5, 65]))

class TestSorting(unittest.TestCase):
    def setup(self):
        pass

    def test_bubble_sort(self):
        self.assertEqual([3,4,5,21,65],bubbleSort([3, 21, 4, 5, 65]))
    
    def test_selection_sort(self):
        self.assertEqual([3,4,5,21,65],selectionSort([3, 21, 4, 5, 65]))

if __name__ == "__main__":
    unittest.main()
