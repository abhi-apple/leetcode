class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=[False]*len(rooms)
        st=[0]
        while st:
            room=st.pop()
            vis[room]=True
            for key in rooms[room]:
                if not vis[key]:
                    st.append(key)
        return all(vis)