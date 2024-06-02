# There are three robots named Ray, Ben and Kevin. Initially Ray has a string S of length N. while the other two robots have empty strings. We can make either of the following moves:
# Move 1: Remove the first character from Ray's string and append it to Ben's string.
# Move 2: Remove the last character from Ben's string and append it to Kevin's string.
# You must perform either of the two moves mentioned above in such a way that the strings left with Ray and Ben are empty and the string left with Kevin is lexicographically the smallest. Your task is to return this lexicographically smallest string that Kevin has after completing this activity.
# Note: For any two given strings, a string is said to be lexicographically smaller than the other if it comes before the other string in the dictionary

from collections import deque

def solve(s):
    ray = deque(s)
    ben = []
    kevin = []

    while ray or ben:
        if not ben:
            ben.append(ray.popleft())
        elif not ray:
            kevin.append(ben.pop())
        else:
            if ray[0] <= ben[-1]:
                ben.append(ray.popleft())
            else:
                kevin.append(ben.pop())

    return ''.join(kevin)


if __name__ == "__main__":
    n = 5
    ray = "abacd"

    ans = solve(ray)
    print(ans)
