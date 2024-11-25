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
private:
    // 트리의 높이를 계산하고 균형 여부를 확인하는 함수
    int checkHeight(TreeNode* root, bool& isBalanced) {
        // 기저 사례: 빈 노드의 경우
        if (root == nullptr) return 0;
        
        // 왼쪽 서브트리의 높이 계산
        int leftHeight = checkHeight(root->left, isBalanced);
        // 오른쪽 서브트리의 높이 계산
        int rightHeight = checkHeight(root->right, isBalanced);
        
        // 높이 차이가 1보다 크면 균형이 맞지 않음
        if (abs(leftHeight - rightHeight) > 1) {
            isBalanced = false;
        }
        
        // 현재 노드를 포함한 높이 반환 (더 큰 높이 + 1)
        return max(leftHeight, rightHeight) + 1;
    }
    
public:
    bool isBalanced(TreeNode* root) {
        bool isBalanced = true;
        checkHeight(root, isBalanced);
        return isBalanced;
    }
};