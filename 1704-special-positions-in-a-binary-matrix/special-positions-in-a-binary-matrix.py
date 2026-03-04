class Solution(object):
    def numSpecial(self, mat):
        onesx = []
        onesy = []
        for ri, rv in enumerate(mat):
            for ci,cv in enumerate(rv):
                if cv == 1:
                    onesx.append(ri)
                    onesy.append(ci)
        count = 0
        for idx in range(len(onesx)):
            if onesx.count(onesx[idx]) == 1:
                if onesy.count(onesy[idx]) == 1:
                    count += 1
        return count