#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re

def getchar(file_name):
    f = open(file_name, "r")
    return len(f.read())

def getline(file_name):
    f = open(file_name, "r")
    read = f.readlines()#以行为单位读取文本并存入列表
    return len(read)

def getword(file_name):
    f = open(file_name, "r")
    read = re.split(r'[^a-zA-Z]+',f.read())
    return len(read)
#拓展功能获取空行，代码行，注释行
def getexpend(file_name):
    f = open(file_name, "r")
    _line = 0 #记录多行注释位置
    line_ = 0
    emptyline = 0 #空行
    codeline = 0  #代码行
    commentline = 0 #注释行
    is_comment = False #多行注释标记
    comment_sign = 0
    read = f.read(). split('\n')
    for line in read:
        _line+=1
        line= line.strip()
        if not is_comment:
            if len(line)<=1:
                emptyline += 1
            elif line.startswith('#'): #检索以'#'开头的单行注释
                commentline += 1
            elif line.startswith("'''") or line.startswith('"""'):
                 comment_sign += 1
                 line_=_line
                 is_comment =True
                 if  comment_sign%2==0 and comment_sign>0:
                     commentline = commentline + _line - line_
                     is_comment = False
                     line_ = _line
            else: codeline += 1
    print('空行数:',emptyline)
    print('代码行数:',codeline)
    print('注释行数:',commentline)

def main():
    str, name = input('输入命令符和文件路径(以空格分开)：\n').split()
    if  str=='-c':
        print('字符数:',getchar(name))
    elif str=='-w':
        print('单词数:',getword(name))
    elif str=='-l':
        print('行数:',getline(name))
    elif str=='-a':
        getexpend(name)
main()