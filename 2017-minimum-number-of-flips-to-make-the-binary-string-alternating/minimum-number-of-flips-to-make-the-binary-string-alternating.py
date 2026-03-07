class Solution(object):
    def minFlips(self, s):
        n=len(s) 
        s+=s 
        ans=sys.maxint 
        ans1,ans2=0,0
        s1=""
        s2=""
        for i in range(len(s)):
            if i%2==0:
                s1+="1"
                s2+="0"
            else :
                s1+="0"
                s2+="1"
        for i in range(len(s)):
            if s[i]!=s1[i]:
                ans1+=1
            if s[i]!=s2[i]:
                ans2+=1
            if i>=n:
                if s[i-n]!=s1[i-n]:
                    ans1-=1
                if s[i-n]!=s2[i-n]:
                    ans2-=1
            if i>=n-1:
                ans=min([ans,ans1,ans2])
        return ans  