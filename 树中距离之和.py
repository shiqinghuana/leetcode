from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:

        tree = [[] for _ in range(N)]
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)

        count = [1]*N
        su=0
        def get_pepth(target=0,depth=0,father="A"):
            nonlocal su
            su +=depth
            for i in tree[target]:
                if i !=father:
                    get_pepth(i,depth+1,target)
                    count[target] +=count[i]

        get_pepth()


        answer = [0] * N
        answer[0]= su
        def get_answer(target=0,father="A"):

            for i in tree[target]:
                if i !=father:
                    answer[i] = answer[target] -2*count[i]+N
                    get_answer(i,target)

        get_answer()
        return answer