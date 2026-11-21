class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        counter1, counter2 = [0] * 26, [0] * 26
        matches = 0
        for i in range(n1):
            counter1[ord(s1[i]) - 97] += 1
            counter2[ord(s2[i]) - 97] += 1
        for i in range(26):
            if counter1[i] == counter2[i]:
                matches += 1
        if matches == 26:
            return True
        l = 0
        for r in range(n1, n2):
            idx = ord(s2[r]) - 97
            counter2[idx] += 1
            if counter1[idx] == counter2[idx]:
                matches += 1
            elif counter2[idx] - 1 == counter1[idx]:
                matches -= 1
            idx = ord(s2[l]) - 97
            counter2[idx] -= 1
            if counter1[idx] == counter2[idx]:
                matches += 1
            elif counter2[idx] + 1 == counter1[idx]:
                matches -= 1
            l += 1
            if matches == 26:
                return True
        return False

            