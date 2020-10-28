class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:


        try:
            n,k = 0,0

            while n<len(name):
                if name[n] == typed[k]:
                    n+=1
                    k+=1
                elif n!=0 and typed[k] == name[n-1]:
                    k+=1
                else:
                    return False

            return all(i == name[-1] for i in typed[k:])
        except:
            return False
