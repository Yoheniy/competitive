class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        i=0
        ans=0
        cn=0

        for j in range(len(tasks)):
            
            if cn==4:
                cn=0
                i+=1
            cn+=1
            if i<len(processorTime):
                ans=max(ans,processorTime[i]+tasks[j])
                print(ans,processorTime[i],tasks[j])
        return ans


        