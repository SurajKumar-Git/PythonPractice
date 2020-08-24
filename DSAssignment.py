from collections import deque
from math import inf
from typing import List, Union


class Question1:

    def __init__(self) -> None:
        self.stack = []
        self.pairs = {"}": "{", ")": "(", "]": "["}

    def is_correct(self, line: str) -> Union[int, str]:
        for i, ch in enumerate(line):
            if ch in "{([":
                self.stack.append(ch)
            elif ch in "})]":
                if self.pairs[ch] == self.stack[-1]:
                    self.stack.pop()
                else:
                    return i+1
        else:
            if self.stack:
                return i+1
            else:
                return "Success"


# line = input()
# print(Question1().is_correct(line))


class Question2:

    def __init__(self, tree: List[int]) -> None:
        self.tree = tree
        self.stack = []
        self.root = tree.index(-1)

    def find_max_height(self) -> int:
        max_height = 0
        self.stack.append((self.root, 1))  # node, level

        while self.stack:
            parent, level = self.stack.pop()
            curr_height = level

            flag = 0  # No child exists
            # find child nodes and
            for i in range(len(self.tree)):
                if self.tree[i] == parent:
                    self.stack.append((i, curr_height+1))
                    flag = 1  # Found Child

            if not flag:  # if no child exists I.e leaf node Then compare current hieght with max hieght
                if max_height < curr_height:
                    max_height = curr_height
        return max_height


# tree = list(map(int, input().split()))
# print(Question2(tree).find_max_height())


class Question4Stack:

    def __init__(self) -> None:
        self.stack = list()

    def push(self, value: int) -> None:
        if self.stack:
            if value > self.maxi:
                modified_value = 2 * value - self.maxi
                self.stack.append(modified_value)
                self.maxi = value
            else:
                self.stack.append(value)
        else:
            self.maxi = value
            self.stack.append(value)

    def pop(self) -> int:
        value = self.stack.pop()
        if value > self.maxi:
            correct_value = self.maxi
            self.maxi = 2 * self.maxi - value
            return correct_value
        else:
            return value

    def max(self) -> int:
        return self.maxi


# s = Question4Stack()
# n = int(input())
# for _ in range(n):
#     action = input().split()
#     if action[0] == "push":
#         s.push(int(action[1]))
#     elif action[0] == "pop":
#         s.pop()
#     else:
#         print(s.max())


class Question5:

    def __init__(self, nums: List[int], m: int):
        self.nums = nums
        self.m = m  # Window Size
        self.n = len(nums)
        self.q = deque()

    def maximum_sliding_window(self) -> List[int]:
        max_list = []

        for i in range(self.m):
            while self.q and self.nums[self.q[-1]] <= self.nums[i]:
                self.q.pop()
            self.q.append(i)

        # First window max value. The queue will always have max in front of the queue
        max_list.append(self.nums[self.q[0]])

        for i in range(self.m, self.n):
            # Remove front element from window, by checking if q contains the front element index
            if self.q and self.q[0] <= (i - self.m):
                self.q.popleft()

            # Same as previous task. Maintain the decreasing order of values in queue
            while self.q and self.nums[self.q[-1]] <= self.nums[i]:
                self.q.pop()
            self.q.append(i)
            max_list.append(self.nums[self.q[0]])
        return max_list


# nums = list(map(int, input().split()))
# window_size = int(input())
# q5 = Question5(nums, window_size)
# print(*q5.maximum_sliding_window())
