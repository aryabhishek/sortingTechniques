class Job:

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


class Solution:

    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda job: job.profit, reverse=True)

        max_deadline = max(job.deadline for job in Jobs)

        days = [0] * max_deadline
        max_profit = 0
        job_count = 0

        for job in Jobs:

            for i in range(job.deadline - 1, -1, -1):
                if days[i] == 0:
                    days[i] = 1
                    max_profit += job.profit
                    job_count += 1
                    break

        return job_count, max_profit


if __name__ == "__main__":
    jobs = [Job(100, 2), Job(19, 1), Job(27, 2), Job(25, 1), Job(15, 3)]
    solution = Solution()
    result = solution.JobScheduling(jobs)
    print(result)