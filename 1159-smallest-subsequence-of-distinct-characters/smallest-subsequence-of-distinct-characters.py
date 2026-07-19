class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {c : 0 for c in s}
        set1 = set()
        st = []
        for c in s:
            freq[c] += 1

        for c in s:
            freq[c] -= 1
            if c in set1:
                continue
            while st and st[-1] > c and freq[st[-1]] > 0:
                set1.remove(st.pop())
            st.append(c)
            set1.add(c)
        return "".join(st)
        