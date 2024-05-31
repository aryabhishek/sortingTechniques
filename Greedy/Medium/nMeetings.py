class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


class Solution:

    def maximumMeetings(self, n, s, e):
        meet = [Meeting(s[i], e[i], i + 1) for i in range(n)]
        meet.sort(key=lambda x: (x.end, x.pos))
        ans = 1
        limit = meet[0].end

        for i in range(1, n):
            if meet[i].start > limit:
                limit = meet[i].end
                ans += 1

        return ans
