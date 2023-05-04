class Solution:
    def predictPartyVictory(self, sen: str) -> str:
        qr = deque()
        qd=deque()
        n=len(sen)
        for i in range(n):
            if sen[i]=='R':
                qr.append(i)
            else:
                qd.append(i)
        while qr and qd:
            rid=qr.popleft()
            did=qd.popleft()
            if rid<did:
                qr.append(rid+n)
            else:
                qd.append(did+n)
        if qr:
            return "Radiant"
        return "Dire"