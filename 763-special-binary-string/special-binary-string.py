class Solution(object):
    def makeLargestSpecial(self, s):
        if len(s)<=2:
            return s
        count=0
        start=0
        subString=[]
        for i in range(len(s)):
            if s[i]=='1':
                count+=1
            else:
                count-=1
            if count==0:
                inside=self.makeLargestSpecial(s[start+1:i])
                subString.append("1"+inside+"0")
                start=i+1
        subString.sort(reverse=True)
        return "".join(subString)