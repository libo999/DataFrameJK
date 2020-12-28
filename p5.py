# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:26:47 2020

@author: Libo

作业题第5题
"""

if __name__ == "__main__":
    task_num = input()
    starttime = input()
    remaining = input()
    task_num = int(task_num)
    starttime = [int(i) for i in starttime.split(' ')]
    remaining = [int(i) for i in remaining.split(' ')]
    # 表示第几天
    day = 0
    # 记录已完成的任务数
    finished = 0
    # 记录每天安排的任务
    plan = []
    max_starttime = max(starttime)
    while finished != task_num:
        # 选出当天可以选择的任务
        if day < max_starttime:
            options_idx = []
            for i in range(len(starttime)):
                if starttime[i] <= day:
                    options_idx.append(starttime.index(starttime[i]))
        else:
            options_idx = [starttime.index(i) for i in starttime]
        # 确定当天安排的任务
        if len(options_idx) > 0:
            options = [remaining[i] for i in options_idx if remaining[i] > 0]
            temp = min(options)
            temp_idx = remaining.index(temp)
            remaining[temp_idx] = temp - 1
            plan.append(temp_idx)
        else:
            # -9表示当天不安排任务
            plan.append(-9)
        finished = len([i for i in remaining if i == 0])
        day = day + 1
    # 计算完成所有任务需要花费的天数
    total_time = 0
    tasks = [starttime.index(i) for i in starttime]
    for t in tasks:
        maxtime = max([i + 1 for i, v in enumerate(plan) if v == t])
        total_time = total_time + maxtime
    # 输出花费的总天数
    # print('Total time:' + str(total_time))
    print(total_time)
