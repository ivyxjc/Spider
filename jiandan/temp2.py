class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        middle_rank=0
        for i in range(len(nums)):
            if nums[i]>=0:
                middle_rank=i
                break
        res=[]
        if(len(nums)<3):
            return []
        try:
            if(nums[middle_rank]==0):
                if(nums[middle_rank+1]==0):
                    if(nums[middle_rank+2]==0):
                        res.append([0,0,0])
        except:
            res=[]
        negative_sum=0

        for i in range(0,middle_rank-1):
            for j in range(i+1,middle_rank):
                negative_sum=nums[i]+nums[j]
                findResRank=self.binary_search(nums,middle_rank,len(nums)-1,-negative_sum)
                if(findResRank==-1):
                    continue
                if(nums[findResRank]==-negative_sum):
                    res.append([nums[i],nums[j],nums[findResRank]])
        positive_sum=0
        for i in range(middle_rank,len(nums)-1):
            for j in range(i+1,len(nums)):
                positive_sum=nums[i]+nums[j]
                findResRank=self.binary_search(nums,0,middle_rank-1,-positive_sum)
                if(findResRank==-1):
                    continue
                if(nums[findResRank]==-positive_sum):
                    res.append([nums[i],nums[j],nums[findResRank]])

        hashList=[]
        finalRes=[]
        for i in range(0,len(res)):
            hash_value=hash(tuple(res[i]))
            if hash_value not in hashList:
                finalRes.append(res[i])
                hashList.append(hash_value)

        return finalRes

    #有序数组二分查找
    def binary_search(self,list,lo,hi,target):

        while(lo<=hi):
            mid=lo+int((hi-lo)/2)
            if(target<list[mid]):
                hi=mid-1
            elif (target>list[mid]):
                lo=mid+1
            else:
                return mid
        return -1



# list1=[0,1,2,3,4,5]
# print(list1[0:3])
# print(list1[3:6])
#
list1=[1,2,3]
list2=[2,3,1]
print(hash(tuple(list1)))
print(hash(tuple(list2)))
for i in range(0,3):
    print(i)
solution=Solution()
list1=[-1, 0, 1, 2, -1, -4]
list2=[4,-2,-9,9,7,9,10,-15,4,-9,-9,8,-6,7,-7,-2,4,-9,-7,-11,13,9,5,-8,10,8,-6,-1,-2,-6,6,-12,7,4,4,-9,-1,-1,-8,10,5,-10,-5,7,12,4,12,-6,10,-10,-2,8,7,10,7,2,-5,9,-14,9,-12,-1,4,2,11,-15,9,-13,-1,-14,4,12,-9,-15,-4,10,4,-7,-11,-9,-1,-6,14,-9,-10,-1,0,-8,-7,-6,8,-12,0,-3,5,-4,-11,-1,-10,4,-8,10,-7,-10,2,4,-14]

res=solution.threeSum(list2)
print(res)
# print(solution.binary_search([-4,-1,-1,0,1,2],3,5,2))
# print(int((5-2)/2))