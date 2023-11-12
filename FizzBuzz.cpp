class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>result;
        for(int i=1;i<=n;i++){
        
            if(i%3==0&&i%5==0){
                result.push_back("FizzBuzz");
                continue;
            }
            if(i%3==0){
                result.push_back("Fizz");
                continue;
            }
            if(i%5==0){
                result.push_back("Buzz");
                continue;
            }
            else{
                string s=to_string(i);
                result.push_back(s);
            }
            
        }
        return result;
    }
};