class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_l=[]
        negative_l=[]
        zero_l=[]
        l=[]
        for i in range(len(nums)):
            if nums[i]<0:
                negative_l.append(nums[i])
            elif nums[i]>0:
                positive_l.append(nums[i])
            else:
                zero_l.append(nums[i])
        i=0
        j=0
        while(i<len(positive_l) or j<len(negative_l)):
            if(i<len(positive_l) and j<len(negative_l)):
                l.append(positive_l[i])
                l.append(negative_l[j])
                i+=1
                j+=1
            elif(i<len(positive_l) and j>=len(negative_l)):
                 l.append(positive_l[i])
                 i+=1
            elif(j<len(positive_l) and i>=len(negative_l)):
                 l.append(negative_l[j])
                 j+=1
            else:
                break
        l+=zero_l
        return l
            


            
        