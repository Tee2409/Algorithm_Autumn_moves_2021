# 知识点
# 1、二叉树 卡特兰数Catalan数
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



# ---------- 题目 ---------
# n个节点的二叉树一共有((2n)!)/(n! * (n+1)!)种 
# 参考链接：https://blog.csdn.net/garrulousabyss/article/details/86619962
# 公式推导参考链接：https://www.cnblogs.com/zyt1253679098/p/9190217.html

# 各排序算法时间、空间复杂度、稳定性
# 参考链接：https://www.runoob.com/w3cnote/ten-sorting-algorithm.html

# 数组 性质 插入删除元素平均时间复杂度o(n) 可以随机访问任何节点 
# 参考链接：https://www.zhihu.com/question/51545092

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
# 倒买战利品
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
