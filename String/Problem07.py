# https://www.acmicpc.net/problem/9935
import sys

read = sys.stdin.readline
string = read().strip()
bom = read().strip()
ans = []

for i, e in enumerate(string):
    ans.append(e)
    j = -1
    cIdx = len(bom) - 1

    if len(ans) >= len(bom) and bom[cIdx] == ans[-1]:
        isSame = False
        tmp = ''
        while cIdx >= 0 and ans[j] == bom[cIdx]:
            if cIdx == 0:
                del ans[j:]
                isSame = True
            cIdx -= 1
            j -= 1
        if not isSame:
            pass

print("".join(ans) if len(ans) != 0 else "FRULA")