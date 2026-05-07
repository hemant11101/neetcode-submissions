class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>mapana;
        for(const auto& c: strs){
            string thisone = c;
            sort(thisone.begin(),thisone.end());
            mapana[thisone].push_back(c);
        }

        vector<vector<string>> result;
        for(auto& pair : mapana){
            result.push_back(pair.second) ;

        }
        return result ;




       
    }
};
