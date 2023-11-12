class Solution {
public:
    int countPrimes(int n) {
        bool v[n+1];
        fill_n(v,n,false);

        int cn=0;
      
        for(int i=2;i<n;i++){
            if(v[i]==true){
                continue;
            }
            for(int j=i+i;j<n;j+=i){
                v[j]=true;
            }}
            for(int i=2;i<n;i++){
                if(v[i]==false){
                    cn++;
                }
            }
    
    return cn;
    }
};