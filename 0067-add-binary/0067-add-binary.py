class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = bin(int(a, 2) + int(b, 2))
        result = format(int(result, 2), 'b')
        return str(result)