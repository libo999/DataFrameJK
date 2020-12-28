# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:37:47 2020

@author: Libo

作业题第7题
"""


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


class graph:
    def __init__(self, num, ma):
        self.edge = {}
        self.dic = [ma] * (num + 1)

    def add(self, u, v, w):
        if u in self.edge:
            self.edge[u].append((v, w))
        else:
            self.edge[u] = [(v, w)]

    def dijkstra(self, start):
        dis = self.dic
        dis[start] = 0
        heap = []
        visit = [0 for i in range(len(dis))]
        for i in self.edge[start]:
            if dis[i[0]] > i[1]:
                dis[i[0]] = i[1]
            heappush(heap, (i[1], i[0]))  # i[1]为该边权值，i[0]为该点，从start点到其余点的边入堆
        while heap != []:
            vic = heappop(heap)  # 弹出最小边
            if visit[vic[1]] == 1:  # 如果该点已经弹出过，则不再松弛
                continue
            visit[vic[1]] = 1  # 记录弹出点
            if vic[1] not in self.edge:  # 防止有向图中出度为0的点
                continue
            for i in self.edge[vic[1]]:
                if dis[i[0]] > dis[vic[1]] + i[1]:  # 判断是否松弛
                    dis[i[0]] = dis[vic[1]] + i[1]  # 松弛边
                    # heapq.heappush(heap, (i[1], i[0]))  # 松弛过边则把新边权值入堆
                    heappush(heap, (i[1], i[0]))  # 松弛过边则把新边权值入堆
        self.dic = dis

    def printf(self):
        result = self.dic[2:]
        for ele in result:
            print(ele, end=' ')


if __name__ == "__main__":
    # # 测试用代码
    # n, m = 6, 9
    # nums = [[1, 2, 2], [1, 4, 7], [1, 6, 8], [2, 3, 10], [2, 5, 1],
    #         [3, 4, 12], [4, 5, 5], [4, 6, 6], [5, 6, 4]]
    # g = graph(n, 1000000000000)
    # for i in nums:
    #     g.add(i[0], i[1], i[2])
    # g.dijkstra(1)
    # g.printf()
    # print()

    # x, y = 7, 12
    # nums_xy = [[1, 2, 7], [1, 2, 10], [1, 4, 6], [2, 3, 1], [2, 4,
    #                                                          5], [3, 4, 2],
    #            [3, 6, 13], [3, 7, 3], [4, 5, 4], [4, 5, 8], [5, 6, 9],
    #            [5, 7, 11]]
    # g2 = graph(x, 9999999999)
    # for num in nums_xy:
    #     g2.add(num[0], num[1], num[2])
    # g2.dijkstra(1)
    # g2.printf()

    # 作业7标准输入
    # 输入无权图相关元素
    size = input()
    size = [int(i) for i in size.split(' ')]
    m, n = size[0], size[1]
    G = []
    for i in range(n):
        ele = input()
        ele = [int(i) for i in ele.split(' ')][0:3]
        G.append(ele)
    # 图实例化
    g = graph(m, 99999999)
    for i in G:
        g.add(i[0], i[1], i[2])
    g.dijkstra(1)
    # 打印结果
    g.printf()
