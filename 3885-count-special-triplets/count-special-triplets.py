class Solution(object):
    def specialTriplets(self, nums):
        prefix_dict,suffix_dict={},{}
        cnt=0
        for i in nums:
            if i not in suffix_dict:
                suffix_dict[i]=1
            else:
                suffix_dict[i]+=1
        for i in nums:
            suffix_dict[i]-=1
            if prefix_dict and i*2 in prefix_dict and i*2 in suffix_dict:
                cnt+=(prefix_dict[i*2]*suffix_dict[i*2])
            
            if i not in prefix_dict:
                prefix_dict[i]=1
            else:
                prefix_dict[i]+=1
        return cnt % (10**9+7)