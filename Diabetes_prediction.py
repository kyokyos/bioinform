#DIY糖尿病预测器，请随访相关专业医师
#algorithm：
#total_points=gender+BMI+waist+age+race+family_gene+blood_pressure+psycho
#(total_points:0-6 low; 7-15 increased; 16-24 moderate; 25-47high)
#BMI=weight(kg)/height(m)**2

#value

gender="male"
height=1.65
weight=62
hypertension="True"
race="Chinese"
family_history="True"
age=65
waist=100
psycho="True"


#points
total_points=0
gender_point=0
hypertension_point=0
race_point=0
family_history_point=0
age_point=0
waist_point=0
BMI_point=0
BMI_value=0
psycho_point=0
diabetes_probability=0


def gender_analysis(gender):
    if gender=="male":
        return 1

    else:
        return 0

gender_point=gender_analysis(gender)

#print "gender_point:",gender_point
   

def blood_pressure_analysis(hypertension):
    if hypertension=="True":
        return 5
    if hypertension=="True":
        return 0

hypertension_point=blood_pressure_analysis(hypertension)
#print "hypertension_point:",hypertension_point



def race_analysis(race):
    if race=="white":
        return 0
    else:
        return 6

race_point=race_analysis(race)
#print "race_point:",race_point



def family_history_analysis(family_history):
    if family_history=="True":
        return 5
    if family_history=="False":
        return 0


family_history_point=family_history_analysis(family_history)
#print "family_history_point:",family_history_point


def age_analysis(age):
    if age<=50:
        return 0
    elif 50<age<=60:
        return 5
    elif 60<age<=70:
        return 9
    else:
        return 13

age_point=age_analysis(age)
#print "age_point:",age_point
   

def waist_analysis(waist):
    if waist<=90:
        return 0
    elif 90<waist<=100:
        return 4
    elif 100<waist<=110:
        return 6
    else:
        return 9


waist_point=waist_analysis(waist)
#print "waist_point:",waist_point



def BMI(height,weight):
    return weight/height**2

BMI_value=BMI(height,weight)
#print "BMI_value:",BMI_value



def BMI_analysis(BMI_value):
    if BMI_value<18.5:
        return 3
    elif 18.5<=BMI_value<25:
        return 0
   
    elif 25<=BMI_value<30:
        return 3

    elif 30<=BMI_value<32:
        return 5

    else:
        return 9

BMI_point=BMI_analysis(BMI_value)
#print"BMI_point:",BMI_point
   


def psycho_analysis(psycho):
    if psycho=="True":
        return 5
    if psycho=="False":
        return 0

psycho_point=psycho_analysis(psycho)
#print "psycho_point:",psycho_point
   


#total_point
total_points=gender_point+hypertension_point+race_point+family_history_point+age_point+\
waist_point+BMI_point+psycho_point
#print "total_points:",total_points

   
def diabetes_prediction(total_points):
    if 0<=total_points<=6:
        return "low"
    elif 6<total_points<=15:
        return "increased"
    elif 15<total_points<=24:
        return "moderate"
    else:
        return "high"


diabetes_probability=diabetes_prediction(total_points)
print "Your diabetes prediction:",diabetes_probability
