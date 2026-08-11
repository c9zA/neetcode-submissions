class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskq = []
        hmap = collections.Counter(tasks)
        for task, freq in hmap.items():
            taskq.append([-freq, tasks])
        heapq.heapify(taskq)
        cpuq = []
        t = 1
        while taskq or cpuq:
            if taskq:
                task = heapq.heappop(taskq)
                task[0]+=1
                if task[0]<0:
                    heapq.heappush(cpuq, (t+n+1, task))
            t+=1
            if cpuq and cpuq[0][0] == t:
                _, task = heapq.heappop(cpuq)
                heapq.heappush(taskq, task)
        return t-1

        