class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                same_line = 2
                if points[j][0] == points[i][0]:  # special case: vertical line
                    slope = float('inf')
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                for k in range(len(points)):
                    if k != i and k != j:
                        if points[k][0] == points[i][0]:  # special case: vertical line
                            if slope == float('inf'):
                                same_line += 1
                        else:
                            if (points[k][1] - points[i][1]) / (points[k][0] - points[i][0]) == slope:
                                same_line += 1
                max_points = max(max_points, same_line)
        return max_points