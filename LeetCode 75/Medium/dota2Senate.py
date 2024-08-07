"""

"""

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        
        # Populate the queues with indices of senators
        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        # Simulate the process of removal
        while r_queue and d_queue:
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            
            if r_index < d_index:
                # R wins this round, push the R index back with a new round index
                r_queue.append(r_index + len(senate))
            else:
                # D wins this round, push the D index back with a new round index
                d_queue.append(d_index + len(senate))
        
        # Determine the winner
        if r_queue:
            return "Radiant"
        else:
            return "Dire"


if __name__ == "__main__":
    solution = Solution()
    print(solution.predictPartyVictory("RDD"))