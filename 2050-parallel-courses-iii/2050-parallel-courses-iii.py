class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        for pre, course in relations:
            graph[course].append(pre)


        course_times = [0] * (n + 1)

        def calculate_course_time(course):

            if course_times[course] > 0:
                return course_times[course]

            pre_max_time = 0

            for pre in graph[course]:
                pre_max_time = max(pre_max_time, calculate_course_time(pre))


            course_total_time = time[course - 1] + pre_max_time


            course_times[course] = course_total_time

            return course_total_time


        max_time = max(calculate_course_time(course) for course in range(1, n + 1))
        return max_time