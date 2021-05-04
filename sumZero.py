class Solution:
    def sumZero(self, n: int) -> List[int]:
        result=[]
        if n%2==0:
            for i in range(math.ceil(-n/2),math.ceil(n/2)+1):
                if i==0:
                    continue
                print(i)
                result.append(i)    
        else:
            for i in range(math.ceil(-n/2),math.ceil(n/2)):
                print(i)
                result.append(i)
        return result
