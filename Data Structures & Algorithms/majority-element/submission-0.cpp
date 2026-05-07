class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> m1;
        int n = nums.size();
        for (auto i : nums) {
            m1[i]++;
            if (m1[i] > n / 2) {
                return i;
            }
        }
        // According to the problem, a majority element always exists, so this will never be reached.
        return -1;
    }
};
