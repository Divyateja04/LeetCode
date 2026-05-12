class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        n=len(tasks)
        min_start=0
        for i in range(n):
            min_start+=tasks[i][0]
        copy=min_start
        for j in range(n):
            if(copy>=tasks[j][1]):
                copy-=tasks[j][0]
            else:
                min_start+=(tasks[j][1]-copy)
                copy=tasks[j][1]
                copy-=tasks[j][0]
        return min_start 