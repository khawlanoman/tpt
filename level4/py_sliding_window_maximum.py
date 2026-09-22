from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    window = deque()

    for i in range(len(nums)):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result