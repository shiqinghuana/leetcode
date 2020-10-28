import copy
from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x=[]

        try:
            self.solveSudoku1(board,x)
        except:
            pass

        for i in range(9):
            for j in range(9):
                board[i][j] = x[0][i][j]

    def solveSudoku1(self,board,x,n=0):

        if set(board[n]) =={"1","2","3","4","5","6","7","8","9"}:
            if n==8:
                x.append(board) #后面引用这里会抛异常，我们只找其中一种情况，调用方处理异常
            n+=1


        for i in range(9):
            if board[n][i] ==".":
                # TODO
                set_sum = self.get_set(n,i,board)
                if not set_sum: # 说明前面肯定有填错了
                    return # 回朔再尝试

                for num in set_sum:
                    c = copy.deepcopy(board) ## 一定要深拷贝，不然传的是引用
                    c[n][i] = num
                    self.solveSudoku1(c,x,n)

                break # 这里break ,因为每次递归都拷贝一个新的数组进去，不需要再原来数组处理
    # 求每个单元格取值范围
    def get_set(self,row,col,board: List[List[str]]):
        real_row = (row//3)*3
        real_col = (col // 3) * 3

        gong = (real_row,real_col,real_row+3,real_col+3)

        ql = {"1","2","3","4","5","6","7","8","9"}

        xy_g = set()

        for i in range(gong[0],gong[2]):
            for j in range(gong[1], gong[3]):
                xy_g.add(board[i][j])

        xy_r = set(board[row])

        xy_c = set()

        for i in range(9):
            xy_c.add(board[i][col])


        qz = (ql-xy_c)&(ql-xy_r)&(ql-xy_g)

        return [i for i in filter(lambda x:x!=".",list(qz))]