学习笔记

递归
本质即是循环，通过循环体来调用自己。

特性：
向下进入到不同的递归层，向上回到原来的一层；
用参数来传递不同层间的变量；
每一层都是独立的，不受其它层的影响；

递归的代码模版，4部分组成：
1. 递归终结条件（recursion terminator）
2. 处理当前层逻辑（process logic  in current level）
3. 下探到下一层（drill down）
4. 清理当前层（reverse the current level status if needed)

# recursion terminator
If level > MAX_LEVEL:
    process_result
    return

# process logic in current level
process(level, data...)

# drill down 
self.recursion(level + 1, p1, ...)

# reverse the current level status if needed

思维要点：
1， 不要人肉递归（最大误区）
2， 找到最近重复子问题
3， 数学归纳法

分治、回溯
本质是递归
