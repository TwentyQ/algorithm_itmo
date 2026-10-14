import sys
sys.setrecursionlimit(10000)


def height(v):
    if v is None:
        return 0
    return v[3]


def upd(v):
    v[3] = 1 + max(height(v[1]), height(v[2]))


def rot_left(a):
    b = a[2]
    a[2] = b[1]
    b[1] = a
    upd(a)
    upd(b)
    return b


def rot_right(a):
    b = a[1]
    a[1] = b[2]
    b[2] = a
    upd(a)
    upd(b)
    return b


def bal(v):
    upd(v)
    b = height(v[2]) - height(v[1])

    if b == 2:
        u = v[2]
        if height(u[2]) - height(u[1]) >= 0:
            return rot_left(v)
        else:
            v[2] = rot_right(u)
            return rot_left(v)

    if b == -2:
        u = v[1]
        if height(u[2]) - height(u[1]) <= 0:
            return rot_right(v)
        else:
            v[1] = rot_left(u)
            return rot_right(v)

    return v


def add(v, x):
    if v is None:
        return [x, None, None, 1]
    if x == v[0]:
        return v
    if x < v[0]:
        v[1] = add(v[1], x)
    else:
        v[2] = add(v[2], x)
    return bal(v)


def delete(v, x):
    if v is None:
        return None

    if x < v[0]:
        v[1] = delete(v[1], x)
        return bal(v)
    if x > v[0]:
        v[2] = delete(v[2], x)
        return bal(v)

    if v[1] is None:
        return v[2]
    if v[2] is None:
        return v[1]

    m = v[2]
    while m[1] is not None:
        m = m[1]
    v[0] = m[0]
    v[2] = delete(v[2], m[0])
    return bal(v)


def exists(v, x):
    while v is not None:
        if x == v[0]:
            return True
        if x < v[0]:
            v = v[1]
        else:
            v = v[2]
    return False


def next_key(v, x):
    ans = None
    while v is not None:
        if v[0] >= x:
            ans = v[0]
            v = v[1]
        else:
            v = v[2]
    return ans


def prev_key(v, x):
    ans = None
    while v is not None:
        if v[0] <= x:
            ans = v[0]
            v = v[2]
        else:
            v = v[1]
    return ans


def preorder(v, res):
    if v is None:
        return
    res.append(str(v[0]))
    preorder(v[1], res)
    preorder(v[2], res)


q = int(input())
root = None

for i in range(q):
    s = input().split()
    cmd = s[0]

    if cmd == "add":
        x = int(s[1])
        root = add(root, x)
    elif cmd == "del":
        x = int(s[1])
        root = delete(root, x)
    elif cmd == "exists":
        x = int(s[1])
        if exists(root, x):
            print("YES")
        else:
            print("NO")
    elif cmd == "next":
        x = int(s[1])
        r = next_key(root, x)
        if r is None:
            print("None")
        else:
            print(r)
    elif cmd == "prev":
        x = int(s[1])
        r = prev_key(root, x)
        if r is None:
            print("None")
        else:
            print(r)
    elif cmd == "root":
        if root is None:
            print("Empty")
        else:
            print(root[0])
    elif cmd == "height":
        print(height(root))
    elif cmd == "print":
        res = []
        preorder(root, res)
        if len(res) == 0:
            print("Empty")
        else:
            print(" ".join(res))