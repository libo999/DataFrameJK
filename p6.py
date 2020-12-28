# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:16:24 2020

@author: Libo

作业题第6题
"""


# 这一列中，找最大值，同时记录起点，终点
# 因为传进来的是列的前缀和，所以返回的起点、终点代表的是行坐标
def getMax(nums):
    n = len(nums)
    maxVal, curSum = nums[0], nums[0]  # 初始化最大值
    startIndex, end, start = 0, 0, 0  # 初始化临时起点，起点，终点
    for i in range(1, n):
        if curSum < 0:  # 前缀和小于0了，前面就不要了，从当前开始
            curSum = nums[i]
            startIndex = i  # 前面的前缀和小于0了，需要重置起点，从当前开始才有可能成为最大值
        else:
            curSum = curSum + nums[i]

        if curSum > maxVal:
            maxVal = curSum
            start = startIndex  # 记录下前面的起点，默认0，或者是curSum<0后，重新更新的起点
            end = i  # 终点是当前坐标
    return start, end, maxVal  # 起点，终点，最大前缀和（最大面积）


def getMaxMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    maxArea = float('-inf')  # 最大面积

    for left in range(col):  # 从左到右，从上到下，滚动遍历
        colSum = [0] * row  # 以left为左边界，每行的总和
        for right in range(left, col):  # 这一列每一位为右边界
            for i in range(row):  # 遍历列中每一位，计算前缀和
                colSum[i] += matrix[i][right]
            # 在left，right为边界下的矩阵中，前缀和colSum的最大值
            startX, endX, maxAreaCur = getMax(colSum)
            if maxAreaCur > maxArea:
                maxArea = maxAreaCur    # 更新最大子阵和
    return maxArea


if __name__ == "__main__":
    # 输入矩阵尺寸及其对应元素
    row_col = input()
    row_col = [int(i) for i in row_col.split(' ')]
    rowNum = row_col[0]
    colNum = row_col[1]
    matrix = []
    for i in range(rowNum):
        elem = input()
        elem = [int(i) for i in elem.split(' ')]
        matrix.append(elem)
    # 开始执行主程序
    maxArea = getMaxMatrix(matrix)
    # 输出计算结果
    print(maxArea)
