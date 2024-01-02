class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        index=[0]
        cnzero=0
        cn1=nums.count(1)
        ma=cn1
        for i in range(len(nums)):
            if nums[i]==0:
                cnzero+=1
            else:
                cn1-=1
            sum01=cnzero+cn1
            if sum01>ma:
                index.clear()
                index.append(i+1)
                ma=sum01

            elif sum01==ma:
                index.append(i+1)
            else:
                continue
        return index
            


            



            

        