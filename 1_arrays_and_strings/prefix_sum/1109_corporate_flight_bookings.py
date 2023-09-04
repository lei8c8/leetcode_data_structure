from itertools import accumulate

class Solution:
    def corpFlightBookings(self, bookings, n):
        prefix_sum = [0] * n
        for first, last, num in bookings:
            prefix_sum[first - 1] += num
            if last < n:
                prefix_sum[last] -= num
        return list(accumulate(prefix_sum))