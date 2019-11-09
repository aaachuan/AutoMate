### Pattern Matching with Regular Expressions

#### simple example

字符串查找电话号码，如415-555-4242这种形式。

Python中所有正则表达式的函数都在re模块。

```
import re

# 创建Regex对象
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 向Regex对象的search()方法传入查找的字符串，返回一个Match对象
mo = phoneNumRegex.search('My number is 415-555-4242.')
# 调用Match对象的group()方法，返回实际匹配到的字符串
print('Phone number found: ' + mo.group())

# Phone number found: 415-555-4242

```

#### more pattern matching

- 括号()分组与group():+1:
```
>>> import re
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
>>> mo.group(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
>>>
```
- 管道|匹配多个分组
```
>>> heroRegex = re.compile(r'Batman|Superman')
>>> mo1 = heroRegex.search('Batman and Joker.')
>>> mo1.group()
'Batman'
>>> mo2 = heroRegex.search('Superman and Batman.')
>>> mo2.group()
'Superman'
```
用管道匹配多个模式的一个：
```
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel.')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>> mo.group(0)
'Batmobile'
>>>
```
- 问号?可选匹配
```
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('Absolute Batman')
>>> mo1.group()
'Batman'
>>> mo1 = batRegex.search('Absolute Batwoman')
>>> mo1.group()
'Batwoman'
>>>
```

?可以理解为是匹配这个问号之前的分组0次或者1次

- 星号*匹配0次或多次
```
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'
>>> mo1 = batRegex.search('The Adventures of Batwowowoman')
>>> mo1.group()
'Batwowowoman'
```
- 加号+匹配一次或多次
```
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'
>>> mo2 = batRegex.search('The Adventures of Batwowowoman')
>>> mo2.group()
'Batwowowoman'
>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True
>>>
```
- 花括号{}匹配特定次数
```
>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'
>>> mo2 = haRegex.search('Ha')
>>> mo2.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo2 == None
True
```
