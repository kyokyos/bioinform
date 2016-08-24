# -*- coding: utf-8 -*-
"""
Spyder Editor
APRI和FIB4推测肝纤维化或肝硬化情况
This is a temporary script file.
"""
 
import math
 
#APRI缩写：AST to Platelet Ratio Index
#AST单位iu/l
#PRI单位10**9/L
#如果APRI>2，可能有肝硬化
def APRI(AST,upper_AST,PRI):
    apri=((AST*1.0/upper_AST)*100)/PRI
    return apri
 
 
#FIB-4缩写Fibrosis-4
#age单位：年
#AST和ALT单位：U/L，（U/L和iu/L一般可以通用，前者是中国单位，后者是国际单位）
def FIB4(age,AST,ALT,PRI):
    fib4=(age*AST)/(PRI*math.sqrt(ALT))
    return fib4
     
#肝情况推测
def Liver_condition(apri,fib4):
    if apri>2:
        print ("可能发生肝硬化")
        print("如果是慢性乙肝感染者，需要考虑抗病毒药物治疗")
    if fib4<1.45:
        print("无明显肝纤维化或2级以下肝纤维化（轻度纤维化）")
    if fib4>3.25:
        print("肝纤维化程度为3～4级或以上")
 
#提示
def Print_warming():
    print("因算法不断改进，计算结果仅供参考。请随访感染科或肝病科专业医生")
 
 
def Print_unit():
    print("生化指标来自肝功检测和血常规检测")
    print("AST单位：iu/l")
    print("ALT单位：U/L")
    print("PRI单位：10**9/L")
    print("年龄单位：年")
    print("U/L和iu/L一般可以通用，前者是中国单位，后者是国际单位")
 
#提示
Print_warming()
#输出生化值单位   
print("-"*30)
Print_unit()
print("-"*30)
print("")
print("")
     
#输入参数
print("请输入以下参数（例如10,23.5等等）：")
AST=float(input("天门冬氨酸转移酶值（AST）:"))
upper_AST=float(input("天门冬氨酸转移酶（AST）上限值:"))
ALT=float(input("丙氨酸氨基转移酶值（ALT）:"))
PRI=float(input("血小板计数值（PRI）:"))
age=float(input("年龄:"))
 
apri=APRI(AST,upper_AST,PRI)
fib4=FIB4(age,AST,ALT,PRI)
print("-"*30)
print("")
print("")
print("推测结果:")
#肝情况推测
Liver_condition(apri,fib4)
