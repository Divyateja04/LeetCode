class Solution(object):
    def find(self,index,events):
        l = index+1
        r = len(events)-1
        while l<=r:
            m = (l+r)/2
            if events[m][0]>events[index][1]:
                r = m-1
            else:
                l = m+1
        
        return l

    def call(self,i,events,k,dp):
        if (i,k) in dp:
            return dp[(i,k)]

        if k==0 or i>=len(events):
            dp[(i,k)] = 0
            return 0

        j = self.find(i,events)
        opt1 = events[i][2]+self.call(j,events,k-1,dp)
        opt2 = self.call(i+1,events,k,dp)
        dp[(i,k)] = max(opt1,opt2)
        return dp[(i,k)]

    def maxValue(self, events, k):
        events.sort()
        dp = {}
        return self.call(0,events,k,dp)
        
        