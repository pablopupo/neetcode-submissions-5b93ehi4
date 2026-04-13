class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // we have to make a hash map for value : index
        unordered_map<int, int> prevMap; // value : index
        for (int i = 0; i < nums.size(); i++){
            int value = target - nums[i];
            if (prevMap.find(value) != prevMap.end()) return {prevMap[value], i};
            prevMap.insert({nums[i], i});
        }
        return {};
    }
};
