class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int>result;
     
        for(left;left<=right;left++){
             int pleft=left;
            int rem;
            bool s=true;
               while(pleft){
                    rem=pleft%10;
                    pleft/=10;
                    if(rem==0||left%rem!=0){
                         s=false;
                         break;
                    }
                    
               }
               if(s==true){
                   result.push_back(left);
               }

                
        }
        return result;
    }
};