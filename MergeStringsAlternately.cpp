class Solution {
public:
    string mergeAlternately(string word1, string word2) {
 
         string s="";
         
         if(word1.size()==word2.size()){
              for(int i=0;i<word2.size();i++){
                  s+=word1[i];
                  s+=word2[i];
              }
          
         }
         if(word1.size()>word2.size()){
              for(int i=0;i<word2.size();i++){
                  s+=word1[i];
                  s+=word2[i];
              }
              int j=word2.size();
            while(j!=word1.size()){
              s+=word1[j];
              j++;
         }
         }
          if(word2.size()>word1.size()){
              for(int i=0;i<word1.size();i++){
                  s+=word1[i];
                  s+=word2[i];
              }
              int j=word1.size();
            while(j!=word2.size()){
              s+=word2[j];
              j++;
         }
         }

    return s;
         
       
       
        
    }
};