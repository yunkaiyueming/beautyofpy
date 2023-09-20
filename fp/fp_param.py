# coding=utf8

# higher function
def handle_with_fp(x, y, f):
    return f(x) + f(y)

def is_odd(x):
    return x % 2 == 1


def handel_two_data(x, y):
    return x * 5 - y


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


f = abs
print handle_with_fp(-2, -20, f)
print handle_with_fp(-2, -20, abs)

list_data = [1, 2, 3, 4, -1, -2, -3]
list_str_data = ['bob', 'about', 'Zoo', 'Credit']

print map(f, list_data)
print reduce(handel_two_data, list_data)
print filter(is_odd, list_data)
print sorted(list_str_data, cmp_ignore_case)

print __name__, __package__, __file__
