#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import string

#将一个字符串或者十进制数转为二进制字符串
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])



file(lambda )


fp = open("input")
cin = fp.read()

stdin = [_str.strip() for _str in cin.split('\n')]#按照回车分行，同时去除两端多余空格
stdin = filter(lambda _str : len(_str) != 0, stdin)#剔除无意义空行


dict_lable = {}#label跳转用hash表
pc = 0
lines = []

int2 = functools.partial(int,base=2)#偏函数，用于转化二进制

for each in stdin:
    if ('#' in each): #分离注释和正文
        tmp = each.split('#')
        comment = tmp[-1]
        each = tmp[0]

    if (':' in each):#分离标签和代码
        tmp = each.split(':')
        lable = tmp[0]
        main = tmp[1].strip()
        dict_lable[lable] = pc
    else:
        main = each.strip()

    if len(main.partition(" ")[-1]) > 4: #兼容tab和空格两种缩进
        tmp = main.partition(" ")
    else :
        tmp = main.partition("  ")

    insert = {"operator" : tmp[0].lower() , "variables" : [_str.strip() for _str in tmp[-1].strip().split(',')]}
    lines.append(insert) #需要转译的代码遴选完成
    pc += 4

#各个操作符的信息
Operator = {    "add" : {"type" : 'R' ,"op" : "000000", "Sa" : "00000", "func" : "100000"},
                "sub" : {"type" : 'R' ,"op" : "000000", "Sa" : "00000", "func" : "100010"},
                "lw"  : {"type" : 'I' ,"op" : "100011"},
                "sw"  : {"type" : 'I' ,"op" : "101011"},
                "beq" : {"type" : 'I' ,"op" : "000100"},
                "j"   : {"type" : 'J' ,"op" : "000010"}
            }

#各个变量的信息
Variables = {   "$zero" : "00000",
                "$at"   : "00001",
                "$v0"   : "00010",
                "$v1"   : "00011",
                "$a0"   : "00100",
                "$a1"   : "00101",
                "$a2"   : "00110",
                "$a3"   : "00111",
                "$t0"   : "01000",
                "$t1"   : "01001",
                "$t2"   : "01010",
                "$t3"   : "01011",
                "$t4"   : "01100",
                "$t5"   : "01101",
                "$t6"   : "01110",
                "$t7"   : "01111",
                "$s0"   : "10000",
                "$s1"   : "10001",
                "$s2"   : "10010",
                "$s3"   : "10011",
                "$s4"   : "10100",
                "$s5"   : "10101",
                "$s6"   : "10110",
                "$s7"   : "10111",
                "$t8"   : "11000",
                "$t9"   : "11001"
            }

#为下次做反汇编器留的内存部分
Memory = [0 for i in xrange(32)]

final = []

#汇编开始
pc = 0
for each in lines:
    pc += 4
    opt = each["operator"]
    
    if Operator[opt]["type"] == 'R':#对于R类型指令
        if opt == "add" or opt == "sub":
            op = Operator[opt]["op"]
            rs = Variables[each["variables"][0]]
            rt = Variables[each["variables"][1]]
            rd = Variables[each["variables"][2]]
            Sa = Operator[opt]["Sa"]
            func = Operator[opt]["func"]
            insert = op + rs + rt + rd + Sa + func
            #print insert
    elif Operator[opt]["type"] == "I":#对于I类型指令
        if opt == "beq":
            op = Operator[opt]["op"] 

            #string.zfill(dec2bin(num),5)

            rs = Variables[each["variables"][0]]
            rt = Variables[each["variables"][1]]
            lable = each["variables"][2]
            try:
                dict_lable[lable]
            except KeyError:
                print "=========================="
                print "Warning from Hangzhou Lou"
                print "In line " + str(pc/4 + 1)
                print "lable [" + lable + "] Not found"
                exit()
            Imm = dict_lable[lable] - pc + 4
            #print Imm
            Imm = string.zfill(dec2bin(Imm),16)
            #print Imm
            insert = op + rs + rt + Imm
            
        else : #lw and sw
            
            op = Operator[opt]["op"]
            Imm = each["variables"][1].partition("(")[0]
            Imm = string.zfill(dec2bin(int(Imm,16)),16)
            rs = each["variables"][1].partition("(")[-1][:-1].strip()
            rs = Variables[rs]
            rt = each["variables"][0]
            rt = Variables[rt] 
            insert = op + rs + rt + Imm
            #rs = Variables[each["variables"][0]]
            #rt = Variables[each["variables"][1]]]
    final.append(insert)

print final


#print Variables["$zero"]
#print Operator["add"]

