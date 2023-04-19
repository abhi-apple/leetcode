class UndergroundSystem:
    def __init__(self):
        self.user = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.user[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, prev_time = self.user[id]
        self.dest[(start_station, stationName)].append(t-prev_time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(sum(self.dest[(startStation,endStation)]))/len(self.dest[(startStation,endStation)])

#     def __init__(self):
#         self.dic={}

#     def checkIn(self, idc: int, stationName: str, t: int) -> None:

#         self.dic[idc]=[stationName,'',t,0]

#     def checkOut(self, idc: int, stationName: str, t: int) -> None:
#         self.dic[idc][1]=stationName
#         self.dic[idc][3]=t
        

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         ans=0
#         cnt=0
#         for i in self.dic.values():
#             if i[0]==startStation and i[1]==endStation:
#                 ans+=(i[-1]-i[-2])
#                 cnt+=1
        
#         return ans/cnt
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)