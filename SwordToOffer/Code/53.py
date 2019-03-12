# -*- coding:utf-8 -*-
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''


class Solution:
    def __init__(self):
        self.array = []
        self.char = []

    # 返回对应char
    def FirstAppearingOnce(self):
        return self.char[-1]

    def Insert(self, char):

        if char not in self.array:
            if len(self.array)==0:
                self.char.append(char)
            else:
                if len(self.char)>=1 and self.char[-1] == '#':
                    self.char.append(char)
                elif len(self.char)<1 :
                    self.char.append('#')
                else:
                    self.char.append(char)

        else:
            self.char.append(char[-1])
        self.array.append(char)

s=Solution()
s.Insert('g')
print s.FirstAppearingOnce()
s.Insert('o')
print s.FirstAppearingOnce()
s.Insert('o')
print s.FirstAppearingOnce()
s.Insert('g')
print s.FirstAppearingOnce()