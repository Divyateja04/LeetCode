class Solution(object):
    def spellchecker(self, wordlist, queries):
        v="aeiou" 
        exact=set(wordlist)
        cap={} 
        for w in wordlist:
            l=w.lower() 
            if l not in cap:
                cap[l]=w
        vowel={} 
        for w in wordlist:
            pattern=""
            for c in w.lower(): 
                if c in v: 
                    pattern+="*" 
                else:
                    pattern+=c
            if pattern not in vowel:
                vowel[pattern]=w
        r=[] 
        for q in queries:
            if q in exact:  
                r.append(q)
            elif q.lower() in cap:
                r.append(cap[q.lower()])
            else: 
                p=""
                for c in q.lower():
                    if c in v:
                        p+="*"
                    else:
                        p+=c
                if p in vowel:
                    r.append(vowel[p])
                else:
                    r.append("")
        return r 