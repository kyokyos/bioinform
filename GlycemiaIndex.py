#糖尿病血糖指数分析
#glycemia index
#age_analysis,

# input values
glycemia_index=7
diabetes_type="type1"  #type1,type2,none
age=25          #child,adult
test_time="before_meal"  #before_meal, twoHour_after_meal

#other values
age_index="child"
result="normal"

def age_analysis(age):
    if age<18:
        return "child"

    else:
        return "adult"

#age_index
age_index=age_analysis(age)
#print "age_index:",age_index

#analysis if the glycemia index from you is norm
def glycemia_target(age_index,diabetes_type,glycemia_index,test_time):
    #none diabetes
    if diabetes_type=="none":
        #before meal
        if test_time=="before_meal":
            if 3.5<=glycemia_index<=5.5:
                return "normal"
            elif glycemia_index<3.5:
                return "hypoglycemia"
            else:
                return "hyperglycemia"

        #after meal
        if test_time=="twoHour_after_meal":
            if glycemia_index<=8:
                return "normal"
            else:
                return "hyperglycemia"

    # type2
    if diabetes_type=="type2":
        #before meal
        if test_time=="before_meal":
            if 4<=glycemia_index<=7:
                return "normal"
            elif glycemia_index<3.5:
                return "hypoglycemia"
            else:
                return "hyperglycemia"

        #after meal
        if test_time=="twoHour_after_meal":
            if glycemia_index<=8.5:
                return "normal"
            else:
                return "hyperglycemia"

    #type1
    if diabetes_type=="type1":
        #child
        if age_index=="child":
            #before meal
            if test_time=="before_meal":
                if 3.5<=glycemia_index<=5.5:
                    return "normal"
                elif glycemia_index<3.5:
                    return "hypoglycemia"
                else:
                    return "hyperglycemia"
                
            #after meal
            if test_time=="twoHour_after_meal":
                if glycemia_index<=8:
                    return "normal"
                else:
                    return "hyperglycemia"
                
        #adult
        if age_index=="adult":
            #before meal
            if test_time=="before_meal":
                if 4<=glycemia_index<=7:
                    return "normal"
                elif glycemia_index<4:
                    return "hypoglycemia"
                else:
                    return "hyperglycemia"
            
            #after meal
            if test_time=="twoHour_after_meal":
                if glycemia_index<=9:
                    return "normal"
                else:
                    return "hyperglycemia"
        
            
result=glycemia_target(age_index,diabetes_type,glycemia_index,test_time)
if result!="normal":
    print "warning:"
print "result:",result
