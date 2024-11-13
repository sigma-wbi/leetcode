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
    int cal(TreeNode* root)
    {
        if(root!=nullptr)
        {
            return max(cal(root->left),cal(root->right))+1;
        }
        return 0;
    }
    
    int maxDepth(TreeNode* root) {
        return cal(root);
    }
};