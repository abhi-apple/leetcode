class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lengthOfTrip = [ 0 for _ in range(1001)]
        
        for trip, i, j in trips:
            lengthOfTrip[i] += trip # Increment when passenger is on board
            lengthOfTrip[j] -= trip # decrement when they depart
       
        for passenger in lengthOfTrip:
            capacity -= passenger
            if capacity < 0:
                return False
        return True
            