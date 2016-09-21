'''
上台阶
题目描述

有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或者二级，要走上m级，共有多少走法？注：规定从一级到一级有0种走法。
给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100。为了防止溢出，请返回结果Mod 1000000007的值。
'''
class GoUpstairs:
    def __init__(self):
        self.counts_table=[0,1,2]
    def countWays(self, n):
        if n-1<len(self.counts_table):
            return self.counts_table[n-1]
        if n-1==0:
            return 0
        if n-1==1:
            return 1
        if n-1==2:
            return 2
        num=(self.countWays(n-1)+self.countWays(n-2))%1000000007
        self.counts_table.append(num)
        return num
    
go=GoUpstairs()

n=input()
num=go.countWays(n)
print num