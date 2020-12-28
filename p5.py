# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:26:47 2020

@author: Libo

作业题第5题
"""


def greedy_algorithm_p5(task_num, start_time, lasting_time):
    time_now = 0  # 表示当前时间节点
    task_finished_num = 0  # 已经完成的任务数量
    tasks_list = []  # 每个时间节点安排的任务
    max_start_time = max(start_time)
    while task_finished_num != task_num:
        if time_now < max_start_time:  # 找出当前时刻可以开始的任务列表
            options_index = []
            for i in range(len(start_time)):
                if start_time[i] <= time_now:
                    options_index.append(start_time.index(start_time[i]))
        else:
            options_index = [start_time.index(i) for i in start_time]

        if len(options_index) > 0:  # 确定当前时刻安排的任务（剩余工作量最小的）
            option_tasks = [
                lasting_time[i] for i in options_index if lasting_time[i] > 0
            ]
            temp = min(option_tasks)
            temp_index = lasting_time.index(temp)
            lasting_time[temp_index] = temp - 1
            tasks_list.append(temp_index)
        else:
            tasks_list.append(-999)  # 不安排任务
        task_finished_num = len([i for i in lasting_time if i == 0])
        time_now += 1

    # 计算完成所有任务需要花费的时长
    total_time = 0
    tasks = [start_time.index(i) for i in start_time]
    for task in tasks:
        max_time = max(
            [idx + 1 for idx, val in enumerate(tasks_list) if val == task])
        total_time = total_time + max_time

    return total_time


if __name__ == "__main__":
    # 输入任务数、开始时刻列表和任务持续时间列表
    tasks_num = int(input())  # 任务数
    start_time = input()  # 开始时刻列表
    lasting_time = input()  # 任务持续时间列表
    start_time = [int(i) for i in start_time.split(' ')]
    lasting_time = [int(i) for i in lasting_time.split(' ')]
    # 调用贪心算法，返回总时长
    total_time = greedy_algorithm_p5(tasks_num, start_time, lasting_time)
    print(total_time)
