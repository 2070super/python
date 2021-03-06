dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]  # （dx,dy）是8个方向向量
import numpy as np


def finish5(state, pos, key):
    """
    判断在pos处落子能否成5
    """
    for u in range(4):
        sumk = 1
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if key != state[cur_index]:
                break
            sumk += 1

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if key != state[cur_index]:
                break
            sumk += 1

        if sumk == 5:
            return 1

    return 0


def live4(state, pos, key):
    """
    计算在pos处落子形成活4的数量
    """
    counter = 0
    for u in range(4):  # 4个方向，每个方向最多1个活4
        flag = True
        sumk = 1
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        if sumk == 4:
            counter += 1

    return counter


def chong4(state, pos, key):
    """
    计算在pos处落子形成冲4的数量
    """
    counter = 0
    for u in range(8):  # 8个方向，每方最多1个
        flag = True
        sumk = 0
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if flag or key == state[cur_index]:
                if key != state[cur_index]:
                    if flag and state[cur_index] != 0:
                        sumk -= 10
                    flag = False
                sumk += 1
            else:
                break

        if (cur < 0).any() or (cur > 14).any():
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if key != state[cur_index]:
                break
            sumk += 1

        if sumk == 4:
            counter += 1

    return counter - 2 * live4(state, pos, key)


def live3(state, pos, key):
    """
    计算在pos处落子形成活3的数量
    """
    counter = 0

    for u in range(4):  # 三连的活三
        flag = True
        sumk = 1
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        i += 1
        cur = pos + [i * dx[u], i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        i += 1
        cur = pos + [-i * dx[u], -i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue

        if sumk == 3:
            counter += 1

    for u in range(8):  # 非三连的活三
        sumk = 0
        flag = True

        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if flag or key == state[cur_index]:
                if key != state[cur_index]:
                    if flag and state[cur_index] != 0:
                        sumk -= 10
                    flag = False
                sumk += 1
            else:
                break
        if (cur < 0).any() or (cur > 14).any():
            continue
        i -= 1
        cur = pos + [i * dx[u], i * dy[u]]
        cur_index = tuple(cur)
        if state[cur_index] == 0:
            continue

        # sumk sub
        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        if sumk == 3:
            counter += 1

    return counter


def mian3(state, pos, key):
    """
    计算在pos处落子形成眠3的数量
    """
    counter = 0
    for u in range(8):
        sumk = 0
        flag = True
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if flag or key == state[cur_index]:
                if key != state[cur_index]:
                    if flag and state[cur_index] != 0:
                        sumk -= 10
                    flag = False
                sumk += 1
            else:
                break
        if (cur < 0).any() or (cur > 14).any():
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if key != state[cur_index]:
                break
            sumk += 1

        if sumk == 3:
            counter += 1
    return counter - live3(state, pos, key)


def live2(state, pos, key):
    """
    计算在pos处落子形成活2的数量
    """
    counter = 0

    for u in range(4):  # 二连的活二
        sumk = 0
        flag = True
        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        i += 1
        cur = pos + [i * dx[u], i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue
        i += 1
        cur = pos + [i * dx[u], i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        i += 1
        cur = pos + [-i * dx[u], -i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue
        i += 1
        cur = pos + [-i * dx[u], -i * dy[u]]
        cur_index = tuple(cur)
        if (cur < 0).any() or (cur > 14).any():
            continue
        if state[cur_index] != 0:
            continue

        if sumk == 2:
            counter += 1

    for u in range(8):  # 非二连的活二
        sumk = 0
        flag = True

        for i in range(1, 6):
            cur = pos + [i * dx[u], i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                break
            if flag or key == state[cur_index]:
                if key != state[cur_index]:
                    if flag and state[cur_index] != 0:
                        sumk -= 10
                    flag = False
                sumk += 1
            else:
                break
        if (cur < 0).any() or (cur > 14).any():
            continue
        i -= 1
        cur = pos + [i * dx[u], i * dy[u]]
        cur_index = tuple(cur)
        if state[cur_index] == 0:
            continue

        for i in range(1, 6):
            cur = pos + [-i * dx[u], -i * dy[u]]
            cur_index = tuple(cur)
            if (cur < 0).any() or (cur > 14).any():
                flag = False
                break
            if key != state[cur_index]:
                if state[cur_index] != 0:
                    flag = False
                break
            sumk += 1
        if not flag:
            continue

        i += 1
        cur = pos + [-i * dx[u], -i * dy[u]]
        cur_index = tuple(cur)
        if state[cur_index] == 0:
            continue

        if sumk == 2:
            counter += 1
    return counter


if __name__ == '__main__':
    board = np.zeros((15, 15))
    # board[3:6, 3] = 1
    # board[3, 3] = 1
    # board[3:6, 3] = 1
    # board[3, 3] = 1
    board[4:8, 3] = 1
    board[3, 3] = 2

    # board[5, 5] = 1
    # board[6, 6] = 1
    # board[7, 7] = 1
    print(board)
    print(finish5(board, np.array([9, 3]), 1))
