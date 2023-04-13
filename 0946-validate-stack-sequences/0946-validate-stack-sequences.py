class Solution:
    def validateStackSequences(self, pu: List[int], po: List[int]) -> bool:
        st=[]
        j=0  # Move j outside of the for loop to prevent resetting it on each iteration
        for i in pu:
            st.append(i)
            while st and  po[j]==st[-1]:
                st.pop()
                j+=1
                if j==len(po):  # Fix the comparison to len(po) instead of len(po)-1
                    return True
        return False  # Add a check to ensure stack is empty and all elements of po have been processed
