## Leetcode965 ##
class Solution(object):
    def isUnivalTree(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1
        
       ## DFS的基本思路 ##
深度优先遍历图的方法是:从图中某顶点vv出发：

（1）访问顶点vv；

（2）依次从vv的未被访问的邻接点(adjacentadjacent)出发，对图进行深度优先遍历；直至图中和vv有路径相通的顶点都被访问；

（3）若此时图中尚有顶点未被访问，则从一个未被访问的顶点出发，重新进行深度优先遍历，直到图中所有顶点均被访问过为止。　当然，当人们刚刚掌握深度优先搜索的时候常常用它来走迷宫.事实上我们还有别的方法，那就是广度优先搜索(BFS).
————————————————
版权声明：本文为CSDN博主「sooner高」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/g11d111/article/details/75645970
