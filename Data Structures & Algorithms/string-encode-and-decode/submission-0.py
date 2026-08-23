class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''
        for s in strs:
            str_len=len(s)
            encoded_string+=str(str_len)+'#'+s
        return encoded_string
    def decode(self, s: str) -> List[str]:
        extracted_string=''
        decoded_string=[]
        skip_length=0
        i=0
        while i<len(s):
            extracted_string=''
            if s[i]!='#':
                skip_length=skip_length*10+int(s[i])
                i+=1
            elif s[i]=='#':
                i+=1
                for j in range(skip_length):
                    extracted_string += s[i+j]
                decoded_string.append(extracted_string)
                i+=skip_length
                skip_length=0
        return decoded_string