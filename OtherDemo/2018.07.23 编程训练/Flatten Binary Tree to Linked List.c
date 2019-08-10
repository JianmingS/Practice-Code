//
//  Flatten Binary Tree to Linked List.c
//  tryC
//
//  Created by Jianming Shi on 2018/7/22.
//  Copyright © 2018年 Jianming Shi. All rights reserved.
//
/*
 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
 */
#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void flatten(struct TreeNode* root) {
    if (NULL == root)
    {
        return;
    }
    if (NULL != root->left)
    {
        flatten(root->left);
    }
    if (NULL != root->right)
    {
        flatten(root->right);
    }
    struct TreeNode* right_node = root->right;
    root->right = root->left;
    root->left = NULL;
    struct TreeNode* ptr = root;
    while(NULL != ptr->right)
    {
        ptr = ptr->right;
    }
    ptr->right = right_node;
}

int main()
{
    return 0;
}
