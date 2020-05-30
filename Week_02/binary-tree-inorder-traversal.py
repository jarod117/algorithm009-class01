# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归的方法
# 定义一个递归函数，从根节点开始，遍历每一个子节点，如果在某一个子节点没有值，返回上一节点的值；

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         def helper(root):
#             print(f'root value #1: {root}')
#             if not root:
#                 print(f'root value #2: {root}')
#                 return
#             # res.append(root.val) # 前序遍历时，先返回根节点的值
#             helper(root.left)
#             res.append(root.val) # 中序遍历时
#             print(f'res: {res}')
#             helper(root.right)
#             # res.append(root.val) #后序遍历
#         helper(root)
#         return res

# 迭代的方法
# 设置一个变量ptr当作指针，指向根节点，从根节点开始，先遍历所有左子树，将所有左子树，压入栈，直到某个节点不在包含左子树，则将栈中元素依次弹出。然后再将右子树节点值压入栈再弹出；

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        ptr = root
        while ptr or stack:
            while ptr:
                stack.append(ptr)
                # print(f"stack: {stack}")
                ptr = ptr.left
            ptr = stack.pop()
            res.append(ptr.val)
            # print(f"res value: {res}")
            ptr = ptr.right
        return res

