# https://www.acmicpc.net/problem/16434
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
rooms = [list(map(int, read().strip().split())) for _ in range(n)]


def game(max_hp):
    hp = max_hp
    atk = m

    for t, a, h in rooms:
        if t - 1:
            atk += a
            hp = min(max_hp, hp + h)
        else:
            # monster - a 공격 h 생
            atk_cnt = h // atk
            atk_cnt += 1 if h % atk else 0

            m_cnt = hp // a
            m_cnt += 1 if hp % a else 0

            if atk_cnt > m_cnt:
                return False
            hp -= a * (atk_cnt - 1)
    return True


l, r = 1, 123456 * 1000000 * 1000000
ans = 0
while l <= r:
    mid = (l + r) // 2
    if game(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
