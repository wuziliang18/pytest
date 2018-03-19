#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from functools import reduce
# reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）与下一个元素一同执行一个二元的func函数
list = [1, 2, 3, 4, 5]    
print (reduce(lambda x, y:x*10 + y, list,0))
