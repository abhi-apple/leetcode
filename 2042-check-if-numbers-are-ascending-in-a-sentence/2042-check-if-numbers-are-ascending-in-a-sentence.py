class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1

        for w in s.split():
            if w.isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)

        return True