import heapq
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def tell(i,j): 
            return float(i+1)/(j+1)-float(i)/j
        h=[] 
        for j in range(len(classes)): 
            t=tell(classes[j][0],classes[j][1])
            heapq.heappush(h,(-t,j)) 
        for i in range(extraStudents):
            m,c=heapq.heappop(h) 
            classes[c][0]+=1
            classes[c][1]+=1
            n=tell(classes[c][0],classes[c][1])
            heapq.heappush(h,(-n,c)) 
        s=0 
        for i in range(len(classes)):
            s+=float(classes[i][0])/classes[i][1]
        return s/len(classes) 