'''
��̨��
��Ŀ����

��һ¥�ݹ�m�����տ�ʼʱ���ڵ�һ������ÿ��ֻ�ܿ���һ�����߶�����Ҫ����m�������ж����߷���ע���涨��һ����һ����0���߷���
����һ��������int n���뷵��һ������������¥�ķ�ʽ������֤nС�ڵ���100��Ϊ�˷�ֹ������뷵�ؽ��Mod 1000000007��ֵ��
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