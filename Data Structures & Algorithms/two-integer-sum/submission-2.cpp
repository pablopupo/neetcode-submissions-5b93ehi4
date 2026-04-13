class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> maps; // val : index
        for (int i = 0; i < nums.size(); i++){
            int value = target - nums[i];
            if (maps.find(value)!=maps.end()) {
                return {maps[value], i};
                }
            maps.insert({nums[i], i});
        }
        return {};  
    }
};
