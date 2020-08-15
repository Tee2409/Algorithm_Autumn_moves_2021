# --------- 知识点 ---------
# 1、二叉树 卡特兰数Catalan数 二叉树高度
# 2、排序算法
# 3、数组和链表性质
# 4、阈值与召回率关系
# 5、（star）数据label不平衡采取下采样，对预测概率p(label=1)的影响
# 6、AUC计算
# 7、混淆矩阵相关计算
# 8、DNN模型 数据规范化原因
# 9、学习率大小对目标函数的影响
# 10、（star）online learning
# 11、dropout的keep prob与正则化、训练及错误率关系
# 12、有监督和无监督学习 （ps扩展：生成式模型、判别式模型）
# 13、MapReduce相关知识
# 14、栈 进出栈顺序判定
# 15、循环队列
# 16、BFS DFS
# 17、梯度下降（GD） 随机梯度下降（SGD） mini-batch GD
# 18、模型受特征波动范围较大影响较小 树类的模型


# ---------- 题目 ---------
# n个节点的二叉树一共有((2n)!)/(n! * (n+1)!)种 
# 参考链接：https://blog.csdn.net/garrulousabyss/article/details/86619962
# 公式推导参考链接：https://www.cnblogs.com/zyt1253679098/p/9190217.html

# 一个高度为 100 的二叉树最小元素数目是 100
# 考查二叉树高度 

# 各排序算法时间、空间复杂度、稳定性
# 参考链接：https://www.runoob.com/w3cnote/ten-sorting-algorithm.html
# 快排（递归实现）时间复杂度 平均为O(nlogn) 最坏O(n^2) 空间复杂度O(logn) n为节点数

# 数组 性质 插入删除元素平均时间复杂度o(n) 可以随机访问任何节点 
# 参考链接：https://www.zhihu.com/question/51545092

# 设循环队列中数组的下标范围是 1～n，其头尾指针分别为 f 和 r，则其元素个数为 (r-f+n) mod n
# 循环队列 f < r 时 元素个数r-f ，f > r 时  r-f+n 因此为 (r-f+n) mod n

# 二分类 阈值降低 召回率提高 反之，降低。召回率=预测为正的数量/真实为正的数量 分母不变，阈值降低分子增大因此recall提升

# 已知数据集，有label (0, 1) ,  当对该数据训练回归模型时，正样本全部选用， 负样本随机抽取10%， 经过训练得到模型 F， 当F 对某样本 X 预估 p (label = 1)  = 0.6 时，求如果不进行负样本抽样p (label = 1)   约为多少？
# 已知y/(0.1x+y)=0.6，求y/(x+y)=0.13

# 对于样本 (A, B, C, D, E) , 已知其对应的label为 (0, 1, 1 ,0 ,1)，模型A的预估值为 (0.2, 0.4, 0.7, 0.3, 0.5), 模型 B 的预估值为(0.1, 0.3, 0.9, 0.2, 0.5)，请问模型 A 和 模型 B 的 AUC 哪个更高
# 一样 AUC计算公式参考：https://blog.csdn.net/qq_22238533/article/details/78666436

# 一个service 的请求可以被多核并行处理的， 当qps = 100 的时候 4 core  cpu利用率 （40% ）, 平均相应时间 53ms， 当qps = 150 的时候 cpu利用率 （60 % ), 平均相应时间大约是多少？
# 70ms qps是每秒查询率 相当于要处理的任务 任务从100变成150 效率从40变成60 时间从53变成多少? 53*（150/100）=80最接近70,因为CPU利用率的提高并不会增加并发数，而qps=并发数/响应时间

# 在训练过程中，Dropout会让输出中的每个值以概率keep_prob变为原来的1/keep_prob倍，以概率1-keep_prob变为0。也就是在每一轮的训练中让一些神经元随机失活，从而让每一个神经元都有机会得到更高效的学习，会让网络更加健壮，减小过拟合。
# 在预测过程中，不再随机失活，也不在扩大神经元的输出。
# 参考：https://www.cnblogs.com/mfryf/p/11381266.html

# 小红书的笔记一共有14种一级类目，要你设计一个变量存储每个笔记的类目归属，哪些类型可以存储？
# string、enum、char、int8

# K-means 无监督学习 KNN有监督学习

# 关于BFS和DFS正确的是
# 对于图、数的存储结构，BFS、DFS都可以遍历全部节点

# Mini- batch 的梯度下降 单次 iteration 速度比批梯度下降快
# Mini- batch 比随机梯度下降噪声更小

# --------- 编程题 ---------
# 小红书2020 算法卷3
# 笔记草稿
s=input().strip()
a=[]
left=0
for i in s:
    if i=='(':
        left+=1
        continue
    if left:
        if i==')':
            left-=1
        continue
    if i=='<':
        a.pop()
    else:
        a.append(i)
s=''.join(a)
print(s)
# 小红书2020 算法卷3
# 笔记精选
[n] = list(map(int,input().strip().split()))
arr = list(map(int,input().strip().split()))
if n == 1:
    print(arr[0],end=' ')
    print(1)
elif n == 2:
    print(max(arr),end=' ')
    print(1)
else:
    dp = [0]*(n+1)
    dpnum = [0]*(n+1)
    dp[1],dpnum[1] = arr[0],1
    for i in range(2,n+1):
        if dp[i-1] < dp[i-2] + arr[i-1]:
            dp[i] = dp[i-2] + arr[i-1]
            dpnum[i] = dpnum[i-2] + 1
        else:
            dp[i] = dp[i-1]
            dpnum[i] = dpnum[i-1]
    print(dp[-1],dpnum[-1])
# 倒买战利品 算法卷3
n=int(input())
a=[[int(i) for i in input().split()]for _ in range(n)]

a=sorted(a)
a=[i[1]for i in a]
f = [0]*len(a)
ans = 0
for i in a:
    l = 0
    r = ans
    while l < r:
        m = (l + r) >> 1
        if f[m] < i:
            l = m + 1
        else:
            r = m
    f[l] = i
    if l == ans:
        ans += 1
print(ans)

# 字符串倒序 算法卷1
arr = list(map(str,input().strip().split()))
#print(arr)
s=''
for i in range(len(arr)-1,-1,-1):
    s = s + arr[i] + ' '
print(s)

# 击败怪物
"""
参考：
链接：https://www.nowcoder.com/questionTerminal/e93f31a0387b40e88a53e55b8ab703f8
来源：牛客网

考察点：二分搜索、贪心
参考了@Cyan1956大佬的代码，python实现

思路：沿着[0,max_hp]的范围搜索最合适的伤害值，注意对一些特殊情形的处理。
使用函数check_valid判断当前技能伤害能否过关
首先是根据法力值的大小先对整体的怪物进行伤害，只求打满最大的伤害而不去补刀
之后根据剩余的血量重排序，此时：
如果没有了法力值，则只需要判断血量和是不是大约剩余轮数。
如果剩余法力值，则根据重排序的结果，优先清掉血量高的怪物，之后再判断剩余的轮数够不够清掉所有的怪物。
"""
def check_valid(num, turn, magic, hps, damage):
    # 使用技能造成伤害但不补刀，最后剩下法力值的时候在进行补刀
    i = 0
    for i in range(num):
        # 释放技能的次数为整除的次数或者是魔力值的次数，取小的那个

        spell_time = min(hps[i] // damage, magic)
        hps[i] -= spell_time * damage
        turn -= spell_time
        magic -= spell_time
        if magic == 0: break
    # 去除刚好整除的值

    hps = sorted(hps)
    i = 0
    if hps[-1] == 0:return True
    while hps[i] == 0:
        i += 1
    hps = hps[i:]
    # 普攻或者技能能够清掉

    if sum(hps) <= turn : return True
    if len(hps) <= magic:
        return True

    # 还剩余法力值，此时怪物的血量必定都小于技能伤害，按血量从高到低使用技能

    else:
        last = len(hps) - 1
        while magic > 0:
            last -= 1
            magic -= 1
            turn -= 1
        # 无法力值，判断能否用普攻清完

        hps = hps[:last+1]
        return turn >= sum(hps)


def main():
    num, turn, magic = list(map(int, input().split()))
    hps = list(map(int, input().split()))

    #回合不够必定输

    if len(hps) > turn: return -1

    # 法力值为零且血量和大于回合数 必定输
    if magic == 0 and sum(hps) > turn: return -1

    left, right = 0, int(max(hps))
    while left < right:
        mid = (left + right) // 2
        # 注意python浅拷贝的坑

        if check_valid(num, turn, magic, hps.copy(), damage=mid):
            right = mid
        else:
            left = mid+1
    # 如果left = max(hps)，同样是不存在伤害值满足条件，left一直右移直到越界

    return left if left < max(hps) else -1

print(main())
