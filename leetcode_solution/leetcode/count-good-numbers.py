class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7 
        def my_pow(base, exponent):
            if exponent==0:
                return 1
            result=my_pow(base,exponent//2)
            result*=result
            result%=MOD
            if exponent%2==1:
                result*=base
            result%=MOD
            return result
        even=(n//2)+(n%2)
        odd=n//2
        return (my_pow(5, even) * my_pow(4, odd))% MOD