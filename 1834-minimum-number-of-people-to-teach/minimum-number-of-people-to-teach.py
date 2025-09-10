class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        m = len(languages)
        lang_sets = [set(lang) for lang in languages]
        must_teach = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if lang_sets[u] & lang_sets[v]:
                continue  
            must_teach.add(u)
            must_teach.add(v)
        if not must_teach:
            return 0
        lang_count = [0] * (n + 1)  
        for user in must_teach:
            for lang in lang_sets[user]:
                lang_count[lang] += 1
        max_known = max(lang_count)
        return len(must_teach) - max_known