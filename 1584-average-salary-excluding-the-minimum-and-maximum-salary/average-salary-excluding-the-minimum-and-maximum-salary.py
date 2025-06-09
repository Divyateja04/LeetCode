class Solution(object):
    def average(self, salary):
        avg=0
        salary.sort()
        for i in range(1,len(salary)-1):
            avg+=salary[i]
        return float(avg)/float(len(salary)-2)