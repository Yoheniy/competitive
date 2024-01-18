class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def getmax(answerKey:str,k:int,char):
            left=0
            count=0
            ans=0
            for right in  range(len(answerKey)):
                if answerKey[right]==char:
                    count+=1
                while count>k:
                    if answerKey[left]==char:
                        count-=1
                    left+=1
                ans=max(ans,right-left+1)
            return ans
        answer=max(getmax(answerKey,k,'T'),getmax(answerKey,k,'F'))
        return answer

    