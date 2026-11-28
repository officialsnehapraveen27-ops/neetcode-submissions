class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=""

        for word in strs:

            n=len(word)
            encoded+=str(n)+"#"+word

        return encoded

    def decode(self, s: str) -> List[str]:

        decoded=[]
        
        i=0

        while i < len(s):

            j=i


            while s[j]!="#":

                j+=1

            l= int(s[i:j])
            start=j+1
            end=start+l
            word=s[start:end]

            decoded.append(word)
            

            i=end
            

        return decoded
