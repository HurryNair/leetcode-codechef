# Unsure of exact question title on leetcode
# n1 = [1,0,4,5]
# n2 = [2,3,4]

# Your task is to add these 2 and return [1,2,7,9]

def addNumsAsList(l1, l2):
    l1 = toNum(l1)
    l2 = toNum(l2)

    l3 = l1 + l2
    l3_list = [int(x) for x in str(l3)]
    
    return l3_list


def toNum(l):
    return(int("".join(str(x) for x in l)))

if __name__ == "__main__":
    l1 = [1,0,4,5]
    l2 = [2,3,4]
    print(addNumsAsList(l1, l2))
