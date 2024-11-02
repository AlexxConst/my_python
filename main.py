class Solution(object):
    def makeFancyString(self, s):
        s = s.lower()
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                count = min(stack[-1][1] + 1, 1)
                stack[-1] = (char, count)
            else:
                stack.append((char, 1))

        result = "".join(char * count for char, count in stack)
        return result


solution = Solution()

res = solution.makeFancyString('Heeellllooo wooorrrrlllddd')
print(res)
