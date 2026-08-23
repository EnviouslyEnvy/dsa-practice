class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # If it's a power of four, its bits should look like #000000000000, #0000000000, #00, #0000, #000000
        # We can get rid of sums by checking if it's also a power of 2
        # 1431655765, 0x55555555, 1010101010101010101010101010101
        return (n==n & 1431655765) and (n & (n - 1)) == 0 and n!=0