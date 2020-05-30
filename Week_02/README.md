学习笔记

1. 哈希表
也叫散列表，根据关键码值而直接进行访问的数据结构。（看起来像是python的字典。）
它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
这个映射函数叫做散列函数（Hash function），存放记录的数组叫做哈希表（或散列表）。

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dicts = collections.defaultdict(int)
        for i in range(len(s)):
            dicts[s[i]] = dicts[s[i]] + 1
            dicts[t[i]] = dicts[t[i]] - 1
        for val in dicts.values():
            if val != 0:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s: tracker[x] += 1
        for x in t: tracker[x] -= 1
        return all(x == 0 for x in tracker.values())
        
defaultdict还可以被用来计数，将default_factory设为int即可。
collections.defaultdict(int)

default_factory设为set时，可以用defaultdict建立集合字典（a dictionary of sets）。
collections.defaultdict(set)

default_factory设为list时，可以很容易将键-值对序列转换为列表字典。
collections.defaultdict(list)

collections.Counter()可以用来统计某个列表中，各个元素出现的次数。
collections.Counter(nums) #这里Counter统计列表nums中各个元素出现的次数。

python给字典排序-sorted方法
https://www.py.cn/faq/python/12154.html

2. 树、二叉树、二叉搜索树
链表是特殊化的树，即链表是只有一个子节点的树，因为单链表只有一个next指针
树是特殊化的图，即树是没有环的图

二叉树遍历
1. 前序(Pre-order)： 根-左-右
2. 中序(In-order)： 左-根-右
3. 后序(Post-order)： 左-右-根

二叉搜索树
是指一颗空树，或者具有下列性质的二叉树
1. 左子树上所有结点的值都小于根结点的值；
2. 右子树上所有结点的值都大于根结点的值；
3. 以此类推： 左右子树也分别为二叉查找树（重复性！！！）

中序遍历： 升序遍历

堆 heap
Heap： 可以迅速找到一堆数中的最大或最小值的数据结构
将根节点最大的堆叫做大顶堆或大根堆，将根节点最小的堆叫做小顶堆或小根堆。
常见的堆有二叉堆、斐波那契堆等。

假设是大顶堆，常见操作的复杂的：
find-max：           O(1)
delete-max：         O(logn)
insert (create)：    O(logn) or O(1)

二叉堆性质
通过完全二叉树来实现 （不是二叉搜索树）
二叉堆（大顶）满足下列性质：
1. 是一颗完全树；
2. 树中任意节点的值总是>=其子节点的值；

二叉堆实现细节
1. 二叉堆一般都是通过“数组”来实现

2. 假设“第一个元素”在数组中的索引为0的话(顶堆元素即根节点是：a[0])，则父节点和子节点的关系如下：
a. 索引为i的左孩子的索引是(2*i+1)
b. 索引为i的右孩子的索引是(2*i+2);
c. 索引为i的父节点的索引是floor((i-1)/2);

图
DFS代码 - 递归写法
visited = set() # 和树中的DFS最大区别

def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return
    
    visited.add(node)
    
    # process current node here
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
            
BFS代码
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    
    visited = set() # 和树中的BFS最大区别
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)


python内置方法创建堆有两种方式，heappush()和heapify()

'''
heapq模块提供了堆队列算法的实现，也称为优先级队列算法。
要创建堆，使用初始化为[]的列表，或者可以通过函数heapify()将填充列表转换为堆。
提供一下功能：
将值项推入堆中，保持堆不变。
heapq.heappush (堆，项目)
在线性时间内，将列表x转化为堆。
heapq.heapify (x)
弹出并返回堆中的最小项，保持堆不变。如果堆是空的，则引发IndexError。
heapq.heappop (堆)
'''
import heapq

#1. heappush生成堆 + heappop把堆从小到大pop出来
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
for i in data:
    heapq.heappush(heap, i)
print(heap)

lis = []
while heap:
    lis.append(heapq.heappop(heap))
print(lis)    
#输出结果
[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2. heapify生成堆 + heappop把堆从小到大pop出来
data2 = [1,5,3,2,9,5]
heapq.heapify(data2)
print(data2)

lis2 = []
while data2:
    lis2.append(heapq.heappop(data2))
print(lis2)
#输出结果
[1, 2, 3, 5, 9, 5]
[1, 2, 3, 5, 5, 9]

#1. heapq.nlargest(n, iterable[, key])
从迭代器对象iterable中返回前n个最大的元素列表，其中关键字参数key用于匹配是字典对象的iterable，用于更复杂的数据结构中。

#2. heapq.nsmallest(n, iterable[, key])
从迭代器对象iterable中返回前n个最小的元素列表，其中关键字参数key用于匹配是字典对象的iterable，用于更复杂的数据结构中。


python中operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
k = [3,6,8]
b = operator.itemgetter(2,0) # 定义函数b，获取对象的第2和0个域的值
print(b(k))
#输出(8, 3)
https://www.cnblogs.com/mululu/p/10538695.html
https://www.cnblogs.com/zhoufankui/p/6274172.html