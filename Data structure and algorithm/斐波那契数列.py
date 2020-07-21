# coding: utf-8
"""Fibonacci sequence (recursive / memo / two variable record)
time : 2021/07/21
author : Jessy
# 斐波那契数列(递归/备忘录(dp)/两变量记录)
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N+）
"""
def fibonacci_recursive(n):
    # 递归 时间复杂度为O(2的n次方) 空间o(n)
    if n < 2:
        return n
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
# sample
print(fibonacci_recursive(3))
def fibonacci_memo2(n):
    # 备忘录 dp 时间、空间复杂度 o(n)
    rs=[0,1]
    if n < 2 :
        return n
    for _ in range(n-2):
        rs.append(rs[-1]+rs[-2])
    return rs[-1]
print(fibonacci_memo(3))
def fibonacci_memo2(n):
    # 两变量记录 优化 时间、空间复杂度 o(n) o(1)
    a,b=0,1
    if n < 2 :
        return n
    for _ in range(n):
        a,b=b,a+b
    return a
print(fibonacci_memo2(3))
