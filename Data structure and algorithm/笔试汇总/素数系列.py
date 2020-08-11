# 哥德巴赫猜想：任何大于2的偶数可以表示成两个素数的和。（参考链接：https://zhuanlan.zhihu.com/p/54219387）
# 素数：指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。

# ---------- 与素数有关的题目 ----------
# 1、判断一个整数是否为素数
# 2、判断n及n以下的整数有多少个素数（or 有哪些素数）（变形：给n个数，找出其中所有素数，并求和）
# 3、判断区间[a,b]间有多少个素数（or 有哪些素数 or素数之和） 参考：https://www.cnblogs.com/Renqy/archive/2020/04/19/12732155.html
# 4、判断一个整数是否可以由两个素数相加得到（变形：给一个数，可以由多少对素数之和得到，eg.10=2+5=3+7,结果为2）
# 5、判断一个整数是否可以由若干个素数相加得到，若可以，给出所有情况
# 6、判断一个整数是否可以由若干个素数相加得到，若可以，给出素数个数最多的数量,eg=
# 7、一个整数分解成若干个素数相乘
# 8、回文素数 leetcode886
# 9、丑数 剑指offer49

# ------------------------------------
# ---------------1、判断一个整数是否为素数
# 调用math模块 用除法遍历到sqrt(n) 时间复杂度O(sqrt(n))
import math
def is_prime(n):
    if n < 2:return False
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
# test
is_prime(5)
# 不调用模块 时间复杂度O(sqrt(n))
def is_prime(n):
    if n < 2 or n == 4:return False
    if n == 3:return True
    i = 2
    while i*i < n:
        if n % i == 0:
            return False
        i += 1
    return True
is_prime(16)
