class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        temp = []

        for b in s:
            if b == "(":
                temp.append(")")
            elif b == "{":
                temp.append("}")
            elif b == "[":
                temp.append("]")
            elif b in [")", "}", "]"]:
                if not temp or temp.pop() != b:
                    return False
        return not temp