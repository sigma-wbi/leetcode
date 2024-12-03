/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if(root == NULL) return vector<int>();
        // 왼쪽 자식 -> 오른쪽 자식 -> 자기 자신
        vector <int> totalTraversal;
        vector <int> leftTraversal = postorderTraversal(root->left);
        vector <int> rightTraversal = postorderTraversal(root->right);
        totalTraversal.insert(totalTraversal.end(), leftTraversal.begin(), leftTraversal.end());
        totalTraversal.insert(totalTraversal.end(), rightTraversal.begin(), rightTraversal.end());
        totalTraversal.push_back(root->val);
        return totalTraversal;
    }
};