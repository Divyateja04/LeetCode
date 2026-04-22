class Solution(object):
    def twoEditWords(self, queries, dictionary):
        r=[]
        for q in queries:
            for d in dictionary:
                c=0
                for i in range(len(q)):
                    if q[i]!=d[i]:
                        c+=1
                if c<=2:
                    r.append(q)
                    break
        return r