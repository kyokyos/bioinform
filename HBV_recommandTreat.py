# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 08:51:16 2016
参数太多，改为excel表单填写参数，防止各种异常
@author: daxiong
"""
 
import math,xlrd
 
excelFilename="HBV检测参数.xlsx"
sheetName="Sheet1"
#打开excel数据
excelFile=xlrd.open_workbook(excelFilename)
   
sheet=excelFile.sheet_by_name(sheetName)
#翻译后放入的列表
translation_list=[]
#获取第一行的值
row1_values=sheet.row_values(0)
row2_values=sheet.row_values(1)
list_row1_row2=list(zip(row1_values,row2_values))
 
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
def Liver_damage(apri,fib4):
    if apri>2:
        print ("可能发生肝硬化")
        print("如果是慢性乙肝感染者，需要考虑抗病毒药物治疗")
        return True
    if fib4<1.45:
        print("无明显肝纤维化或2级以下肝纤维化（轻度纤维化）")
        return False
    if fib4>3.25:
        print("肝纤维化程度为3～4级或以上")
        print("如果是慢性乙肝感染者，需要考虑抗病毒药物治疗")
        return True
         
         
#是否慢性乙肝
#positive_HBsAg_time 表示hbv表明抗原持续时间
def CHB(positive_HBsAg_persistTime):
    if positive_HBsAg_persistTime>6:
        return True
    else:
        return False
             
         
#是否该用抗病毒药治疗
def Recommand_treat(chb,apri,HBV_DNA,year,persist_abnormal_ALT):
    if chb==True and apri>2:
        return True
    if chb==True and apri<=2 and year>30 and HBV_DNA>20000 and persist_abnormal_ALT==True:
        return True
         
#持续观察
def Recommand_surveillance_noTreat(chb,apri,HBV_DNA,year,persist_abnormal_ALT,discontinuous_abnormal_ALT,positive_HBeAg):
         
    if chb==True and apri<=2 and persist_abnormal_ALT==True and HBV_DNA<2000:
        return True
    if chb==True and year<=30 and apri<=2 and HBV_DNA>20000 and persist_abnormal_ALT==False:
        return True
         
    if chb==True and positive_HBeAg==False and apri<=2 and year<=30 and 2000<HBV_DNA<20000 and discontinuous_abnormal_ALT==True:
        return True
         
         
     
def Recommand_drug(year):
     
    if year >=12:
        drug=["Tenoforvir(泰诺福韦)","entecavir(恩替卡韦)"]
    if 2<=year <=11:
        drug="entecavir(恩替卡韦)"
    
   
    return drug   
          
#提示
def Print_warming():
    print("因算法不断改进，计算结果仅供参考。请随访感染科或肝病科专业医生")
    print("单一测试可能受到酒精，情绪，气温等多种因素影响，请结合弹力成像，B超等结果综合判断")
    print("肝功观察需要三个月时间，排除酒精，情绪，气温等其它因素造成")
 
#各生化指标单位
def Print_unit():
    print("生化指标来自肝功检测和血常规检测")
    print("AST单位：iu/l")
    print("ALT单位：U/L")
    print("PRI单位：10**9/L")
    print("年龄单位：年")
    print("U/L和iu/L一般可以通用，前者是中国单位，后者是国际单位")
    print("HBV_DNA单位：IU/mL")
 
#最后汇总
def Print_summary(recommand_treat,recommand_surveillance_noTreat):
    if recommand_treat==True:
        print("推荐抗病毒药治疗")
        print("推荐药物：",drug)
        print("药物推荐来自《世界卫生组织2015乙肝指南》")
        print("服用核苷酸药物前，应检查肾功能")
    if recommand_surveillance_noTreat==True:
        print("推荐继续观察，暂时不需用药")
         
 
#输出logo
def Print_logo():
    print("问题反馈邮箱：231469242@qq.com")
    print("                  .-.     ")
    print("                   \ \    ")
    print("                    \ \   ")
    print("   喵  喵 喵          | |  ")
    print("                     | |  ")
    print("   /\---/\   _,---._ | |  ")
    print("  /^   ^  \,'       `. ;  ")
    print(" ( O   O   )           ;  ")
    print("  `.=o=__,'            \  ")
    print("    /         _,--.__   \  ")
    print("   /  _ )   ,'   `-. `-. \ ")
    print("  / ,' /  ,'        \ \ \ \  ")
    print(" / /  / ,'          (,_)(,_) ")
    print("(,;  (,,)                    ")
    var=input("按任意键退出") 
 
#提示
Print_warming()
#输出生化值单位   
print("-"*30)
Print_unit()
print("-"*30)
print("")
print("")
     
#从excel内获取参数，避免异常输入
AST=list_row1_row2[0][1]
upper_AST=list_row1_row2[1][1]
ALT=list_row1_row2[2][1]
PRI=list_row1_row2[3][1]
year=list_row1_row2[4][1]
positive_HBsAg_persistTime=list_row1_row2[5][1]
HBV_DNA=list_row1_row2[6][1]
persist_abnormal_ALT=list_row1_row2[7][1]
discontinuous_abnormal_ALT=list_row1_row2[8][1]
positive_HBeAg=list_row1_row2[9][1]
 
      
#是否慢性乙肝   
chb=CHB(positive_HBsAg_persistTime) 
apri=APRI(AST,upper_AST,PRI)
 
recommand_treat=Recommand_treat(chb,apri,HBV_DNA,year,persist_abnormal_ALT)
recommand_surveillance_noTreat=Recommand_surveillance_noTreat(chb,apri,HBV_DNA,year,persist_abnormal_ALT,discontinuous_abnormal_ALT,positive_HBeAg)
drug=Recommand_drug(year)
 
 
#最后汇总
Print_summary(recommand_treat,recommand_surveillance_noTreat)
 
print("-"*30)
print("")
print("")
Print_logo()
