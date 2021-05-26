'''
第一题：招聘候选人
题目描述
计算公司一轮招聘过程中，未完成招聘计划的部门数量，以及参与该公司招聘但未被录用的候选人人数。

每个部门的招聘计划人数 存储在非负整数数组 nums 中，数组下标即为部门的编号；
每位候选人的考试成绩 存储在非负整数数组 scores 中，数组下标即为候选人的编号；
每位候选人可以选则至少1个或多个意向部门，候选人选择的意向部门 存储在二维数组 preference 中，数组一维下标即为候选人的编号；
函数返回一个整数数组，依次记录未完成招聘计划的部门数量、未被录用的候选人人数。

录取规则
编号小的部门具有更高的优先录用权，每个部门仅能录用对该部门有意向的候选人，按照候选人成绩从高到低完成录用，
如果候选人成绩相同，则优先录用编号较小的候选人
每个候选者最多只能被一个部门录用 (一旦被高优先级的部门录用，则低优先级的部门不能再录用该候选人)

示例1
输入:

nums = [1, 2, 1]
scores = [67, 58, 89, 42, 27]
preference = [[0, 1], [1], [0, 2], [2], [0]]
输出:

[0, 1]
示例2
输入:

nums = [3, 2, 0]
scores = [67, 89, 67, 42]
preference = [[2, 1], [1], [1, 2], [1]]
输出:

[1, 2]
注意
部门的招聘计划可以为0，也视为完成了招聘计划
'''
from operator import itemgetter
from collections import defaultdict

class Solution:
    def employee(self, nums, scores, preference):
        people_num = len(scores)
        people_flag = [0 for _ in range(people_num)]
        departs = 0
        
        depart_selects = defaultdict(list)
        for i, pre in enumerate(preference):
            for p in pre:
                depart_selects[p].append((i, scores[i]))
            
        for i, num in enumerate(nums):
            left = num
            if left == 0:
                departs += 1
                continue
            
            for p in sorted(depart_selects[i], key=lambda x: (-x[1], x[0])):
                no, score = p
                if people_flag[no] == 1:
                    continue
                
                people_flag[no] = 1
                left -= 1
                if left == 0:
                    departs += 1
                    break
       
        no_people = 0 
        for p in people_flag:
            if p == 0:
                no_people += 1
                
        return [departs, no_people]
            
            
if __name__ == "__main__":
    nums = [1, 2, 1]
    scores = [67, 58, 89, 42, 27]
    preference = [[0, 1], [1], [0, 2], [2], [0]]

    print(Solution().employee(nums, scores, preference))