# ------- 知识点 ------
# 1、经典问题：扔鸡蛋问题变形
# 2、深度学习梯度消失
# 3、过拟合问题
# 4、项目介绍
# 5、动态规划
# 6、字符串排序

# 问答题
# 1、黑客入侵点定位

"""
题目：
150个代码模块按顺序串行执行组成，某一个模块突然被黑客入侵（当前模块也称入侵点）。
现存两款从不同角度设计的反入侵检测程序，
1.输入：顺序代码段，必须以模块1开始（比如：模块1->模块2->…模块39）
2:输出：True-输入包含入侵点，False-输入不包含入侵点
3.每款检测程序可以运行多次：可多次返回False,但仅能返回一次True（由于入侵的对抗性存在，一旦输出True即报废，后续检测功能失效）
4.同一时刻只能有一款检测程序运行，每检测一次耗时10分钟
现在希望仅利用现有的两款反入侵检测程序，在最短的时间内确保可以快速定位入侵点。具体需要如何设计检测流程，时间是多久。
"""
# 分析：二分法 用第一个检测仪器确定是哪几个串联模块（集合A）出的问题 第二个检测仪器一次检查前述的几个模块
# 假设第k次二分找到集合A 花费10k分钟 集合A大小为size=150//(2**k) 因此还需花费10*size分钟
# 共需花费10(k+size)分钟  

# 深度学习训练中梯度消失的原因有哪些？有哪些解决方法？
"""
原因：
（1）某些激活函数 例如sigmoid函数在x远离0的位置处于饱和区 梯度变化非常小 随着网络层数的增加 产生梯度消失现象
解决方法：
（1）选用ReLU、leaklyReLU等函数，在x>0和x<0时梯度恒定为常数，缓解梯度消失问题
（2）采用Batch Normalization Layer调整经过激活函数的数据分布变化，缓解梯度消失问题
（3）减少网络层数
"""

# 过拟合问题
# 在做项目或者参加比赛的时候，经常会遇到过拟合的问题。结合你的实际经历，讲讲你是怎么理解过拟合以及怎么解决过拟合问题的？
"""
过拟合：
在训练集上进行过度学习，除了数据集上的通用性质以外过多的学习细节内容，具体表现为训练集上效果好，但测试集上效果差
如何解决过拟合：
（1）在损失函数上添加正则化项，例如l1、l2
（2）增加训练集样本，对样本进行剪裁、旋转、放缩、重采样等技术扩充样本数量
（3）树模型可以减少树棵树、树深度、叶子结点数、采样比例、特征采样比例
（4）深度学习中可以减少网络层数、添加dropout、BN层等
（5）选择复杂度小一点的模型
"""

# 请简述一个你参与过的计算机视觉/语音/自然语言处理/机器学习项目或其他类型重要项目（包括项目的应用场景，行业现状及主流解决方案，你的解决方案），描述你在完成项目的过程中遇到的技术问题，以及你的解决思路与方法。
# 根据个人项目自由发挥

# 工作安排
# dp问题
[n] = list(map(int,input().strip().split()))
task =[]
for i in range(n):
    task.append(list(map(int,input().strip().split())))
dp = [0]*(n+1)
dp[1]=max(task[0][0],task[0][1])
for i in range(2,n+1):
    dp[i]=max(dp[i-1]+task[i-1][0],dp[i-2]+task[i-1][1])
print(dp[-1])

# 字符串排序 基数排序
def solution(data):
    lc = list('abcdefghijklmnopqrstuvwxyz ')
    lc = lc[::-1]
    dic = {}
    # 生成value为[]的字典
    for i in range(len(lc)):
        dic[i] = []
    # 记录最长的字符串的长度
    maxL = 0
    for i in range(len(data)):
        if len(data[i]) > maxL:
            maxL = len(data[i])
    # 字符串左对齐 右侧补空格
    for i in range(len(data)):
        data[i] = data[i].ljust(maxL, ' ')
    # 倒序 
    for i in range(maxL-1, -1, -1):
        for j in range(len(data)):
            idx = lc.index(data[j][i])
            dic[idx].append(data[j])
            print(dic)
        new_data = []
        for k in dic:
            new_data += dic[k]
            dic[k] = []
        data = new_data
    print(','.join(x.strip() for x in data))


if __name__ == '__main__':
    data = input().strip().split(',')
    solution(data)


# 字符串排序 
def isChange(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i]>str2[i]:
            return 0
        elif str1[i]<str2[i]:
            return 1
    if len(str1) <= len(str2):
        return 0
    else:
        return 1

strings = input().split(',')

str_len = len(strings)
for i in range(0, str_len-1):
    for j in range(i+1, str_len):
        change_flag = isChange(strings[i], strings[j])
        if change_flag:
            tmp = strings[i]
            strings[i] = strings[j]
            strings[j] = tmp
ans = ",".join(strings)
print(ans)
