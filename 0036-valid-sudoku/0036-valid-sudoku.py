class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue

                # Check row
                if char in rows[r]:
                    return False
                rows[r].add(char)

                # Check column
                if char in cols[c]:
                    return False
                cols[c].add(char)

                # Check 3x3 sub-box
                box_index = (r // 3) * 3 + (c // 3)
                if char in boxes[box_index]:
                    return False
                boxes[box_index].add(char)

        return True
