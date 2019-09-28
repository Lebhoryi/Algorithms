# coding=utf-8
'''
@ Summary: 有1-n个人，每个人手中随机的正数密码m，第一个m作为上限，从第一个开始数，
           第m个剔除，接着第m个人的密码作为上限，从第m+1个人开始数，最后全部人剔除队伍结束
@ Update:  

@ file:    2-12.约瑟夫问题（困难级）.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-9-28 下午2:53
'''

class Node(object):
    def __index__(self, val):
        self.val = val
        sslf.next = None

    def __repr__(self):
        return str(self.val)

class LCLink(object):
    @ staticmethod
    def c_link(vals):
        '''Creating link

        :param vals: list
        :return rear: the rear node,尾节点,Node
        '''
        if not vals:
            return None
        
