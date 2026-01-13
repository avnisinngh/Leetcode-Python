class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = float('inf')
        high = float('-inf')
        total = 0.00000

        for square in squares:
            x = square[0]
            y = square[1]
            l = square[2]
            total = total + l*l

            low = min(low,y)
            high = max(high, y+l)
        
        result_y = 0.00000

        def check(squares,mid_y,total):
            bot_area = 0
            for square in squares:
                y = square[1]
                l = square[2]
                boty = y
                topy = y+l

                if mid_y >= topy:
                    bot_area = bot_area + l*l
                elif mid_y > boty:
                    bot_area = bot_area + (mid_y - boty)*l

            return bot_area >= total/2.0

        while(high-low > 1e-5):
            mid_y = low + (high-low)/2
            result_y = mid_y
            if(check(squares, mid_y, total) == True):
                high = mid_y
            else:
                low = mid_y
        return result_y