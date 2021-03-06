# -*- coding: utf-8 -*-

class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []
        ret = []
        level = [root]
        while level:
            ret.append([])
            new_level = []
            for node in level:
                ret[-1].append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level
        ret.reverse() # 反转二叉树的层次遍历
        return ret