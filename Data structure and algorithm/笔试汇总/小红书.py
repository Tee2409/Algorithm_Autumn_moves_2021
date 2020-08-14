# 知识点
# 1、二叉树 卡特兰数Catalan数
# 2、排序算法
# 3、数组和链表性质
# 4、阈值与召回率关系







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
# 
