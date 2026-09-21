from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove indexes that are outside the window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller values from the back
        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        # Add current index
        window.append(i)

        # Start recording maximums once the first window is complete
        if i >= k - 1:
            result.append(nums[window[0]])

    return result