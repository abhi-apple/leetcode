class Solution:
    def leastInterval(self, ts: List[str], n: int) -> int:
        count=Counter(ts)
        maxih=[-cnt for cnt in count.values()]
        heapq.heapify(maxih)
        time=0
        q=deque()
        while maxih or q:
            time+=1
            if maxih:
                cnt=1+heapq.heappop(maxih)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxih,q.popleft()[0])
        return time
                