class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        st=[0]*2
        st[0]=celsius+273.15
        st[1]=celsius*1.80 + 32.00
        return st