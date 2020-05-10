from tree.TreeNode import TreeNode
from typing import List


class Solution:
    """
    中序 递归
    """

    def __init__(self):
        self.return_list = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.return_list.append(root.val)
        self.inorderTraversal(root.right)
        return self.return_list

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.return_list.append(root.val)
        self.inorderTraversal(root.left)
        self.inorderTraversal(root.right)
        return self.return_list

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.inorderTraversal(root.right)
        self.return_list.append(root.val)
        return self.return_list

    def inorderTraversalNoDiGui(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                self.return_list.append(root.val)
                root = root.right
        return self.return_list

    def preorderTraversalNoDiGui(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        while root or stack:
            if root:
                self.return_list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return self.return_list

    """
    类似于层次遍历，只不过是先把右边的先压入桟中，然后出栈就是中左右，正好符合前序访问顺序
    """

    def preorderTraversalNoDiGuiDoubleStack(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            self.return_list.append(root.val)
        return self.return_list

    """
    另一种方法是借助双栈进行处理。我们曾在前序方法一借助一个栈右压，左压。持续让达到一个前序遍历的效果。但是这个方法很难实现后续。

分析相同方法，如果我们先压左，再压右，那么我们获得的顺序将是和前序完全相反的顺序（顺序为：中间，右侧，左侧。倒过来刚好是左侧、右侧、中间的后续）对称看起来的前序。即用另一个栈将序列进行反转顺序！

    """

    def postorderTraversalNoDiGui(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return reversed(res)

    """
    传统后序
    
    而在后序遍历中：它有这样的规则：

    入栈，第一次访问
    即将出栈。第二次访问，
    如果有右孩子，先不出栈把右孩子压入栈第一次访问，如果没右孩子。访问从栈中弹出。
    循环重复，直到栈为空
    """

    def postorderTraversalNoDiGuiTwo(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        count_dict = {}
        while stack or root:
            if root:
                count_dict[root] = 1
                stack.append(root)
                root = root.left
            else:
                t1 = stack[-1]
                if count_dict[t1] == 2:
                    res.append(stack.pop())
                    #root = None
                else:
                    count_dict[t1] = 2
                    root = t1.right

        return res


if __name__ == "__main__":
    s = Solution()
    t = TreeNode()
    print(t.__dict__)
    print(s.inorderTraversal(t.left))
