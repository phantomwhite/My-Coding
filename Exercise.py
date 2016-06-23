# -*- coding: utf-8 -*-

def triangles():
    lst = [1]
    while True:
        yield lst
        lsttemp = lst[:]
        for i in range(len(lsttemp)):
            if i != 0:
                lst[i] = lsttemp[i] + lsttemp [ i - 1]
        lst.append(1)

def normalize(name):
    return name.capitalize()

# ---------------------------------------
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y, L)

#----------------------------------------
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda x : CHAR_TO_FLOAT[x], s)
    point = 0
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        else:
            if point == 0:
                f = f * 10 + n
            else:
                point *= 10
                f = f + n/point
            return f
    return reduce(to_float,nums,0.0)

#------------------------------------------
# 两种方式求回数

# def is_palindrome(n):
#     s = str(n)
#     return s == s[::-1] and len(s) > 1

def is_palindrome(n):
    num = 0
    ntmp = n
    while ntmp > 0:
        num = num * 10 + ntmp % 10
        ntmp //= 10
    return num == n and n > 10
#--------------------------------------------

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
#--------------------------------------------
import functools

def decorat(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call")
        print('call %s():' % func.__name__)
        func()
        print("end call")
    return wrapper
#--------------------------------------------

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

#--------------------------------
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
        return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a + b
            return L
# ------------------------------------------
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    # def __call__(self,path):
    #     return Chain('%s/%s' % (self._path,path))
    def users(self,path):
        return Chain('%s/%s' % (self._path,path))
    # def repos(self,path):
    #     print('repos is :',path)
    __repr__ = __str__

# ----------------------------------
def fact(n):
    '''
    Simp code for fact
>>> fact(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fact(0)
  File "<pyshell#6>", line 3, in fact
    raise ValueError()
ValueError
>>> fact(1)
1
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

# ------------------------------
import threading,multiprocessing
def loop():
    x = 0
    while  True:
        x = x * 1

# -----------------------------
import re
def reIsEmail(s):
    stremail = r'[\w\_]+@[\w]+.[com|net|cn]'
    # liuwh@julong.com.cn 能够匹配 [a-zA-Z0-9\_]+@[a-zA-Z0-9\.]+[com|net|cn]
    return re.match(stremail,s)

# -------------------------------
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity
    
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)

        if containsKey:
            del self[key]
            print('set:', (key,value))
        else:
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)
# ----------------------------
#未完成
import base64
def safe_base64_decode(s):
    n = len(s) % 4
    if n is not 0:
        for i in range(4 - n):
            s.append('=')
    
    base64.encode


# -----------------------------
import struct
def IsBmp(filepath):
    with open(filepath,'rb') as f:
        data = struct.unpack('<ccIIIIIIHH',f.read(30))
        print(data)
        if(data[0] == b'B'):
            print(data[2],data[-1])
# ----------------------------------
import hashlib
def getMd5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    print(md5.hexdigest())
# ----------------------------------
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' %tag)

    def handle_endtag(self,tag):
        print('</%s>' %tag)

    def handle_startendtag(self,tag,attrs):
        print('<%s/>' % tag)

    def handle_data(self,data):
        print(data)

    def handle_comment(self,data):
        print('<!--',data,'-->')

    def handle_entityref(self,name):
        print('&%s;' % name)
    
    def handle_charref(self,name):
        print('&#%s;' % name)

# ----------------------------------------


if __name__ =='__main__':
    # test triangles
    # for i in triangles():
    #     print(i)

    # test normalize
    # L1 = ['adam', 'LISA', 'barT']
    # L2 = list(map(normalize, L1))
    # print(L2)

    # test prod
    #print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

    # test str2float
    # print('str2float(\'123.456\') =', str2float('123.456'))

    # test is_palindrome
    # output = filter(is_palindrome, range(1, 1000))
    # print(list(output))

    # test by_name
    # L2 = sorted(L,key=by_name)
    # print(L2)
    # test by_score
    # L3 = sorted(L,key=by_score)
    # print(L3)

    # test decorat
    # @decorat
    # def func():
    #     print('func calling')
    # func()

    # test Screen
    # s = Screen()
    # s.width = 1024
    # s.height = 768
    # print(s.resolution)
    # assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
    # s.resolution = 100 #无法设置只读属性
    # print(s.resolution)

    # test Chain
    # print(Chain().status.user.timeline.list)
    # print(Chain().users('michael').repos)

    #test fact
    # import doctest
    # doctest.testmod()

    # test loop
    # import threading,multiprocessing
    # threads = []
    # for i in range(multiprocessing.cpu_count()):
    #     t = threading.Thread(target = loop)
    #     threads.append(t)
    #     t.start()
    # # 如果不等待vs自己会退出，无法debug 
    # for i in threads:
    #     i.join()

    # test 测试多进程占用cpu
    # import threading

    # # 创建全局ThreadLocal对象:
    # local_school = threading.local()

    # def process_student():
    #     # 获取当前线程关联的student:
    #     std = local_school.student
    #     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

    # def process_thread(name):
    #     # 绑定ThreadLocal的student:
    #     local_school.student = name
    #     process_student()

    # t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
    # t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # test IsBmp
    #IsBmp(r'F:\structTest.bmp')

    # test hashlib
    #getMd5('phantom_white')

    #test MyHTMLParser
    # parser = MyHTMLParser()
    # parser.feed('''<html>
    # <head></head>
    # <body>
    # <!-- test html parser -->
    #     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
    # </body></html>''')