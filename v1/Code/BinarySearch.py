def binary_search(l, key):
    start = 0
    end = len(l)-1

    while(start <= end):
        mid = int((start + end)/2)
        if key == l[mid]:
            return mid
        elif key > l[mid]:
            start = mid + 1
        elif key < l[mid]:
            end = mid - 1
    
    return -1

if __name__ == "__main__":
    l = [1, 2, 3, 6, 7, 89]
    key = 54
    print(binary_search(l , key))
