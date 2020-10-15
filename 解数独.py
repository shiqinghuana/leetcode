from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x = []
        try:
            self.solveSudoku1(board, x)
        except:
            pass
        for i in range(9):
            for j in range(9):
                board[i][j] = x[0][i][j]
        print(board)

    def solveSudoku1(self, board, x, n=0):

        if set(board[n]) == {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if n == 8:
                x.append(board)
                # 这里不return 拿到值就让抛异常
            n += 1

        for i in range(9):
            # print(n)
            if board[n][i] == ".":  # 找到空
                # TODO doSomething
                set_num = self.get_set(n, i, board)
                if not set_num:  # 找不到合适的值
                    return  # 回朔
                for num in set_num:
                    c = copy.deepcopy(board)
                    # c = board
                    c[n][i] = num
                    self.solveSudoku1(c, x, n)

                break  # 截断，后续空在递归里处理

    # 思路，每行，每列 每宫不能重复，如果重复了就换一个

    # 获取每个单元格能输入值得范围
    def get_set(self, row, col, board: List[List[str]]):
        # 求宫范围坐标

        rel_row = (row // 3) * 3
        rel_col = (col // 3) * 3
        gong = (rel_row, rel_col, rel_row + 3, rel_col + 3,)
        ql = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        xy_g = set()  # 宫,行，列现有值
        for i in range(gong[0], gong[2]):  # 行
            for j in range(gong[1], gong[3]):  # 列
                xy_g.add(board[i][j])

        xy_r = set(board[row])
        xy_c = set()
        for i in range(9):
            xy_c.add(board[i][col])

        qz = (ql - xy_g) & (ql - xy_r) & (ql - xy_c)

        return [i for i in filter(lambda x: x != ".", list(qz))]