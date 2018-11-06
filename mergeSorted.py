from collections import deque


def merge_sorted_lists(left, right):
    result = deque()

    left = deque(left)
    right = deque(right)

    while left and right:
        if left[0] > right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())
    return result + left + right
