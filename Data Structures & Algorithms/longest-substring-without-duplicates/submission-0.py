class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest=0
        n=len(s)

        unique=set()

        i=0
        j=0

        while j < n:

            if s[j] not in unique:

                unique.add(s[j])
                j+=1
            else:

                unique.remove(s[i])
                i+=1
            longest=max(longest,j-i)
        
        return longest
        