class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> v;
        for(int i:nums){
            if (find(v.begin(),v.end(),i)==v.end()){
                v.push_back(i);
            }
            else {
                return true;
            }
        }
        return false;
    }
};