class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def get_real_str(s:str):

            a = ""
            for i in s:
                if i!="#":
                    a +=i
                else:
                    if a:
                        a=a[0:-1]
            return a

        
        return get_real_str(S) ==  get_real_str(T)