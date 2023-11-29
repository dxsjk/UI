# -*- coding: utf-8 -*-
"""
文件：UI/mysql/tests/test_face.py
创建者：QE
诗：
    鲸鱼安慰了大海
            - 燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有的花都会盛开
    不是所有约定的人都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
from mysql.page import Page
from prettytable.prettytable import PrettyTable
import unittest
class TestPage(unittest.TestCase):
    def test_get_work(self):
        with Page() as mysql:
            table=(
                mysql
                .db('worker')
                .get_word('info',show=True)
            )[0]
            row=table[1]
            self.assertIsInstance(row,PrettyTable)