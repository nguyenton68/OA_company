class Solution:
    def eval(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return int(s[0])
        st = []
        ans = 0
        for i in s:
            if i in ['+', '-', '*', '/']:
                if len(st) > 0:
                    a = st.pop()
                    b = st.pop()
                    if i == '+':
                        ans = a+b
                    elif i == '-':
                        ans = b-a
                    elif i == '*':
                        ans = a*b
                    else:
                        ans = int(b/a)
                    st.append(ans)
            else:
                st.append(int(i))
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.eval(['4', '5', '+','3','/'])
    print(res)
