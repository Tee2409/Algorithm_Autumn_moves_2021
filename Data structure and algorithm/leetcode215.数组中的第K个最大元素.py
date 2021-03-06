import random
class Solution:
    """
    a 数组arr
    l r 左右指针
    index 目标索引
    约定 nums不为空
    时间复杂度：O(N)，这里N是数组的长度，需要使用主定理进行分析。
    空间复杂度：O(logN)，原地排序，没有借助额外的辅助空间，但递归需要临时存储空间。
    """
    def quick_sort(self,a,l,r,index):
        q = self.randompartition(a,l,r)
        if q == index:
            return a[q]
        elif q < index:
            return self.quick_sort(a,q+1,r,index)
        else:
            return self.quick_sort(a,l,q-1,index)
        
    def randompartition(self,a,l,r):
        # 生成的随机数n: l <= i <= r
        i = random.randint(l,r)
        # 置换i和r索引对应的数
        a[i],a[r] = a[r],a[i]
        return self.partition(a,l,r)
    def partition(self,a,l,r):
        pivot = a[r]
        i = l-1
        for j in range(l,r):
            if a[j] < pivot:
                i += 1
                a[i],a[j]=a[j],a[i]
        a[i+1],a[r]=a[r],a[i+1]
        return i+1
    def findKthLargest(self,nums,K):
        if not nums or len(nums) < K:return False
        if len(nums) < 2:return nums[0]
        return self.quick_sort(nums,0,len(nums)-1,len(nums)-K)

# test
a=Solution()
print(a.findKthLargest([4,2,7,1,9,10],4))
a=Solution()
print(a.findKthLargest([1],0))
a=Solution()
print(a.findKthLargest([1,3],4))
