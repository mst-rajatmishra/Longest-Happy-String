class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        
        # Loop until all counts are exhausted
        while a > 0 or b > 0 or c > 0:
            # Check the last two characters to avoid creating "aaa", "bbb", or "ccc"
            if len(result) >= 2 and result[-1] == result[-2]:
                # If the last two characters are the same, we must choose a different character
                if result[-1] == 'a':
                    if b > 0:
                        result.append('b')
                        b -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        break  # No more options
                elif result[-1] == 'b':
                    if a > 0:
                        result.append('a')
                        a -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        break  # No more options
                elif result[-1] == 'c':
                    if a > 0:
                        result.append('a')
                        a -= 1
                    elif b > 0:
                        result.append('b')
                        b -= 1
                    else:
                        break  # No more options
            else:
                # If the last two characters are different or there's not enough characters, add the most available
                if a >= b and a >= c:
                    result.append('a')
                    a -= 1
                elif b >= a and b >= c:
                    result.append('b')
                    b -= 1
                else:
                    result.append('c')
                    c -= 1
        
        return ''.join(result)

# Example usage
solution = Solution()
print(solution.longestDiverseString(1, 1, 7))  # Example 1: Output could be "ccaccbcc"
print(solution.longestDiverseString(7, 1, 0))  # Example 2: Output could be "aabaa"
