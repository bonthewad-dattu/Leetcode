class Solution(object):
    def leastInterval(self, tasks, n):
      
        from collections import Counter
        task_count = Counter(tasks).values()
        max_num = max(task_count)
        max_cnt = task_count.count(max_num)
        return max(len(tasks), (max_num - 1) * (n + 1) + max_cnt)