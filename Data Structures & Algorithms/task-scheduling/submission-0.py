class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # how many times each task appears
        count = Counter(tasks)
        
        # remaining count of each task, always sort the task by biggest count
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown_q = deque() # [remaining count, next returning time]

        # if heap is not empty or queue is not empty
        while maxHeap or cooldown_q:

            # run most freq task and put that task to cooldown_q
            time += 1 # +1부터 해야하는 이유는 지금꺼 포함해서 다음 돌아오는 시간을 계산하기 위해.

            # if execution of task is possible
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # we add because cnt is (-)
                if cnt:
                    cooldown_q.append([cnt, time + n])
                
            # if cooldown finishes, add back to heap
            if cooldown_q and cooldown_q[0][1] == time:
                heapq.heappush(maxHeap, cooldown_q.popleft()[0])

        return time
