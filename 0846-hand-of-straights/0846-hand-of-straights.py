from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        
        for i in range(len(hand)):
            if hand[i] in count:
                val=hand[i]
                sz = 0
                
                while  val  in count and sz < groupSize:
                    count[val] -= 1
                    if count[val] == 0:
                        del count[val]
                    sz += 1
                    val+=1
                    
                
                # Check if all required cards were found
                # print(count,sz)
                if sz != groupSize:
                    return False
        
        # Check if there are any remaining cards
        if count:
            return False
        
        return True

                    
                    
                