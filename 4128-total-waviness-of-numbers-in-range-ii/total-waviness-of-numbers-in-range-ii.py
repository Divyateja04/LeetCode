class Solution(object):
    def totalWaviness(self, num1, num2):
        def solve(s):
            s=str(s)
            memo={}
            def dfs(pos,tight,left,middle,length):
                if len(s)==pos:
                    return (1,0)
                if (pos,tight,left,middle,length) in memo:
                    return memo[(pos,tight,left,middle,length)]
                total_sm=0
                total_cnt=0
                limit=int(s[pos]) if tight else 9
                for digit  in range(limit+1):
                    new_tight=tight and digit==limit
                    if length==0 and digit==0:
                        cnt,sm=dfs(pos+1,new_tight,10,10,0)
                        total_sm+=sm
                        total_cnt+=cnt
                    elif length <2:
                        cnt,sm=dfs(pos+1,new_tight,middle,digit ,length +1)
                        total_sm+=sm
                        total_cnt+=cnt
                    else:
                        add=0
                        if (left<middle>digit) or(left>middle<digit):
                            add=1
                        cnt,sm=dfs(pos+1,new_tight,middle,digit,length+1)
                        total_sm+=sm+add*cnt
                        total_cnt+=cnt
                memo[(pos,tight,left,middle,length)]=(total_cnt,total_sm)
                return (total_cnt,total_sm)
            return dfs(0,True,10,10,0)[1]
        val1= solve(num1-1)
        val2=solve(num2)
        return val2-val1