class Solution:
    def convert(self, s: str, numRows: int) -> str:
        np = [[""] * len(s) for _ in range(numRows)]
        row, col = 0, 0

        flag = True
        if numRows == 1:
            return s
        s = iter(s)
        while 1:

            try:
                if row == 0:
                    flag = True

                if row == numRows - 1:
                    flag = False

                # TODO
                np[row][col] = next(s)
                if flag:
                    row += 1
                else:
                    row -= 1
                    col += 1
            except:
                break
        s = ""
        for i in np:
            s += "".join(i)
        return s