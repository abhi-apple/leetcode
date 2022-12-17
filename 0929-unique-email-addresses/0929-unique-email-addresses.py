class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        finm=[]
        for i in emails:
            lc,dc=i.split('@')
            lc = lc.replace('.', '')   
            lc=lc.split('+')[0]
            finm.append(lc + '@' + dc)
        finm=set(finm)
        return len(finm)
            
                