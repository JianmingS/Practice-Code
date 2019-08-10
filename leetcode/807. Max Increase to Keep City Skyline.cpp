class Solution {
public:
    
    
    void maxTopOrBottom(const vector<vector<int>> &grid, vector<int> &max_top_or_bottom) {
        for (int i = 0; i < grid.size(); ++i) {
            const vector<int> &item = grid[i];
            max_top_or_bottom.push_back(*max_element(item.begin(), item.end()));
        }
    }
                                 
    void maxLeftOrRight(const vector<vector<int>> &grid, vector<int> &max_left_or_right) {
        int len = grid[0].size();
        for (int i = 0; i < len; ++i) {
            int max_num = 0;
            for (int j = 0; j < grid.size(); ++j) {
                if (grid[j][i] > max_num) {
                    max_num = grid[j][i];
                }
            }
            max_left_or_right.push_back(max_num);
        }
    }                      
                                 
    void getIncreasedGrid(const vector<vector<int>> &grid, vector<vector<int>> &new_grid, const vector<int> &max_top_or_bottom, const vector<int> &max_left_or_right) {
        int len = grid[0].size();
        for (int i = 0; i < grid.size(); ++i) {
            vector<int> row;
            for (int j = 0; j < len; ++j) {
                row.push_back(min(max_top_or_bottom[i], max_left_or_right[j]));
            }
            new_grid.push_back(row);
        }
    }
                                 
    int get_array_sum(const vector<vector<int>> &array) {
        int sum = 0;
        int len = array[0].size();
        for (int i = 0; i < array.size(); ++i) {
            for (int j = 0; j < len; ++j) {
                sum += array[i][j];
            }
        }
        return sum;
    }              
    
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> max_top_or_bottom, max_left_or_right;
        maxTopOrBottom(grid, max_top_or_bottom);
        maxLeftOrRight(grid, max_left_or_right);
        vector<vector<int>> new_grid;
        getIncreasedGrid(grid, new_grid, max_top_or_bottom, max_left_or_right);
        return get_array_sum(new_grid) - get_array_sum(grid);
    }
};
