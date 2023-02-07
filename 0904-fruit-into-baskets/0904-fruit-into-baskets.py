class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length, win_start = 0, 0
        fruit_freq = {}
        
        for win_end in range(len(fruits)):
            fruit_left = fruits[win_end]
            if fruit_left not in fruit_freq:
                fruit_freq[fruit_left] = 0
            fruit_freq[fruit_left] += 1
            
            while len(fruit_freq) > 2:
                fruit_right = fruits[win_start]
                fruit_freq[fruit_right] -= 1
                if fruit_freq[fruit_right] == 0:
                    del fruit_freq[fruit_right]
                win_start += 1
            
            max_length = max(max_length, win_end - win_start + 1)
        return max_length