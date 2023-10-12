# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def find_peak():
            left, right = 0, mountain_arr.length() - 1

            while left < right:
                mid = left + (right - left) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid

            return left

        def binary_search_left(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)

                if mid_val == target:
                    return mid
                elif mid_val < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        def binary_search_right(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)

                if mid_val == target:
                    return mid
                elif mid_val > target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        peak_index = find_peak()
        left_result = binary_search_left(0, peak_index)
        if left_result != -1:
            return left_result

        right_result = binary_search_right(peak_index, mountain_arr.length() - 1)
        return right_result

