#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import unittest
from mydict import Dict,Student

class TestDict(unittest.TestCase):
    
    def setUp(self):
        print('setup.....')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertTrue('key' in d)
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty

#Student 单元测试

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        s3 = Student('Tom','a')
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
        with self.assertRaises(ValueError):
            s3.get_grade()
