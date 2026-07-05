class Solution:
    def longest_substring_array(self, s:str) -> int:
        char_index = {}
        left = 0
        max_length = 0
        for right, char in enumerate (s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left +1)

        return max_length

if __name__ == "__main__" :
    
    solution = Solution()
    print(solution.longest_substring_array("abcabcbb"))
    print(solution.longest_substring_array("bbbbb"))
    print(solution.longest_substring_array("pwwkew"))
