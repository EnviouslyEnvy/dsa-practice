class Solution:
    def maximum69Number (self, num: int) -> int:
        # num=list(str(num))
        # for i in range(len(num)):
        #     if num[i]=='6':
        #         num[i]='9'
        #         return int(''.join(num))
        # return int(''.join(num))
        num=str(num)
        num=num.replace('6','9',1)
        return int(num)

        # Real solution, I knew this existed but I didn't want to think about the math for this one. Credit CbHu.
        # i = 0 
        # tem = num
        # sixidx = -1 
        # while tem > 0:
        #     if tem % 10 == 6:
        #         sixidx = i  #refresh sixidx when found 6 at large digit.
        #     tem = tem//10
        #     i += 1
        # return (num + 3 *(10**sixidx)) if sixidx != -1 else num