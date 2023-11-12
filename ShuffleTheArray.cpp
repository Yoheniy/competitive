class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int>result;
        for(int i=0;i<n;i++){
           result.push_back(nums[i]);
           i+=n;
           result.push_back(nums[i]);
           i-=n;
        }
        return result;
        
    }
};