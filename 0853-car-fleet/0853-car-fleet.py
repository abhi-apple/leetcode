class Solution:
    def carFleet(self, tar: int, po: List[int], spd: List[int]) -> int:
        pair=[[p,s] for p,s in zip(po,spd)]
        st=[]
        
        for p,s in sorted(pair)[::-1]:
         
            st.append((tar-p)/s)

            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
            
        return len(st)