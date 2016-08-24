#高血压测试_程序分析
#测试结果受到多种因素影响，所以该多测试，然后取平均值，而不是仅仅参考一次结果。
#测试标准mmHg
#测试后，根据输入收缩压和舒张压值判断血压状况，
#如患者的收缩压与舒张压分属不同的级别时，则以较高的分级标准为准。
#单词
#systolic pressure 收缩压
#diastolic pressure 舒张压
#血压水平：normal正常，hypertension高血压，hypotension低血压，
#prehypertension 临界高血压,stage1_hypotension高血压一期，stage2_hypotension
#高血压二期
#脉压=systolic_pressure-diastolic_pressure  （脉压>60标志动脉硬化）
#预防措施

    #保持正常体重（如身体质量指数20-25公斤/米;2).
    #将饮食中钠的摄入量减少至<100毫摩尔/天（每天<6克氯化钠或<2.4克的钠）。
    #定期从事有氧运动，如快走（在一周的大多数日子里，每天≥30分钟）。
    #限制饮酒，男性每天不超过3个单位，妇女每天不超过2个单位。
    #每天的饮食中含丰富的水果和蔬菜（例如，每天至少五份）。
#治疗方案

#要改进

systolic_pressure=120
diastolic_pressure=70
blood_pressure="normal"
systolic_result="normal"
diastolic_result="normal"
systolic_value=0
diastolic_value=0
hypotension_tuple=("hypotension",0)
normal_tuple=("normal",1)
prehypertension_tuple=("prehypertension",2)
stage1_hypotension_tuple=("stage1_hypotension",3)
stage2_hypotension_tuple=("stage2_hypotension",4)

list_bloodType=[hypotension_tuple,normal_tuple,\
            prehypertension_tuple,stage1_hypotension_tuple,\
            stage2_hypotension_tuple]
#print list_type

#收缩压分析
def systolic_analysis(systolic_pressure):
    if systolic_pressure<90:
        return "hypotension"
    elif 90<=systolic_pressure<119:
        return "normal"
    elif 120<=systolic_pressure<139:
        return "prehypertension"
    elif 140<=systolic_pressure<159:
        return "stage1_hypotension"
    else:
        return "stage2_hypotension"



     
def diastolic_analysis(diastolic_pressure):
    if diastolic_pressure<60:
        return "hypotension"
    elif 60<=diastolic_pressure<79:
        return "normal"
    elif 80<=diastolic_pressure<89:
        return "prehypertension"
    elif 90<=diastolic_pressure<99:
        return "stage1_hypotension"
    
    else:
        return "stage2_hypotension"


    
   
#血压评级
def rank(blood_pressure,list_bloodType):
    for i in list_bloodType:
        if blood_pressure==i[0]:
            return i[1]



#舒张压和紧缩压评级比较        
def compare(systolic_value,diastolic_value):
    if systolic_value>diastolic_value:
        return systolic_value
    elif systolic_value<diastolic_value:
        return diastolic_value
    else:  #相等情况
        return systolic_value

#最后两者的评级结果       
   
    
def get_type(compared_value):
    for i in list_bloodType:
        if i[1]==compared_value:
            return i[0]

#收缩压类型
systolic_result=systolic_analysis(systolic_pressure)
#舒张压类型
diastolic_result=diastolic_analysis(diastolic_pressure)
#收缩压评级
systolic_value=rank(systolic_result,list_bloodType)
#舒张压评级
diastolic_value=rank(diastolic_result,list_bloodType)
#比较收缩压和舒张压评级
compared_value=compare(systolic_value,diastolic_value)
#确定评级比较后的类型
blood_pressure=get_type(compared_value)

print "blood_pressure:",blood_pressure
