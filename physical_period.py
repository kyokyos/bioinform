# 运行程序，只需输入某人生日，计算机就可智能列出此人生理周期最值（max,min），并可以图形化展示，抽取部分数据验证，程序计算准确。但仍有一些小瑕疵，以后有空改进。

#time transformation
#common year, month accumulation of days
#python 2.7 import do not support """ """ mark format
import leap_common_year


def total_day_calculate(year,month,day):

    which_year=leap_common_year.leap_common_year(year)

    #for common year
    if which_year[0].lower()=='c':
    
        dict_of_month={"january":0,"feburary":59,"march":90,"april":120,
                       "may":151,"june":181,"july":212,"august":243,"september":273
                       ,"october":304,"november":334,"december":365}  #month means accumulation of days
        for i in dict_of_month:
            if month==i:
                month=dict_of_month[i]
                total_day=month+day
    
                return total_day
        


    #for leap year
    if which_year[0].lower()=='l':
    
        dict_of_month={"january":0,"feburary":60,"march":91,"april":121,
                       "may":152,"june":182,"july":213,"august":244,"september":274
                       ,"october":305,"november":335,"december":366}
        for i in dict_of_month:
            if month==i:
                month=dict_of_month[i]
                total_day=month+day
                return total_day



def number_to_time(year,number):
    which_year=leap_common_year.leap_common_year(year)
    
    #for common year
    if which_year[0].lower()=='c':
        
        dict_of_month={"january":0,"feburary":59,"march":90,"april":120,
                       "may":151,"june":181,"july":212,"august":243,"september":273
                       ,"october":304,"november":334,"december":365} 
        sorted_dict_of_month=sorted(dict_of_month.items(), key=lambda d: d[1]) 

        count=0
        
        for i in sorted_dict_of_month:
            if number<i[1]:
                 
                month=sorted_dict_of_month[count-1][0]
                #print "month:",month
                day=number-dict_of_month[month]
            
                return (month,day) 

            count+=1

            



    #for leap year
    if which_year[0].lower()=='l':
    
        dict_of_month={"january":0,"feburary":60,"march":91,"april":121,
                       "may":152,"june":182,"july":213,"august":244,"september":274
                       ,"october":305,"november":335,"december":366}
        sorted_dict_of_month=sorted(dict_of_month.items(), key=lambda d: d[1]) 

        count=0   
        for i in sorted_dict_of_month:
            
            #print "i:",i
            #print "i[1]:",i[1]
            
            #print "count:",count
           
            
            if number<i[1]:
                #print "i[0]:",i[0]
                #print "i[1]:",i[1]
                
              
                
                month=sorted_dict_of_month[count-1][0]
                #print "month:",month
                day=number-dict_of_month[month]
            
                return (month,day)

            count+=1



#input birth day and period to plot your emotional,intelligent,physical sine curve
#y=sin(Bx+C),
import leap_common_year, day_transformation,math,pylab,numpy

def plot_sine_all(year,month,day):
    B_emotion=(2*math.pi)/23
    B_physical=(2*math.pi)/28
    B_intelligence=(2*math.pi)/33
    
    birthday_number=day_transformation.total_day_calculate(year,month,day)
    
    initial_number_emotion=birthday_number%23    #initial_number是正弦函数起始值
    initial_number_physical=birthday_number%28
    initial_number_intelligence=birthday_number%33

    
    C_emotion=(-B_emotion)*initial_number_emotion
    C_physical=(-B_physical)*initial_number_physical
    C_intelligence=(-B_intelligence)*initial_number_intelligence
    
    #use numpy arange to get an array of float values.
    x_values=numpy.arange(0,366,0.001)              #精确值到1.4秒
    y_values_emotion=numpy.sin(x_values*B_emotion+C_emotion)    #numpy.sin() 表示y值
    y_values_physical=numpy.sin(x_values*B_physical+C_physical)
    y_values_intelligence=numpy.sin(x_values*B_intelligence+C_intelligence)
    
    pylab.plot(x_values,y_values_emotion,'r')                 #plot命令允许绘制二维线图,红色是情绪图，绿色是体力图，蓝色是智力图
    pylab.plot(x_values,y_values_physical,'g')
    pylab.plot(x_values,y_values_intelligence,'b')
    
    pylab.xlabel('x axis')                      #x轴标签命名'x values'
    pylab.ylabel('y axis')                      #y轴标签命名'sin of x'
    pylab.title("red=emotion,green=physical,blue=intelligence")     #图表的题目
    pylab.grid(True)                              #图表添加一个网格
    pylab.show()                                  #展示图表



def plot_sine_single(year,month,day,period):
    B=(2*math.pi)/period
    birthday_number=day_transformation.total_day_calculate(year,month,day)
    initial_number=birthday_number%period    #initial_number是正弦函数起始值
    
    
    C=-B*initial_number
    #use numpy arange to get an array of float values.
    x_values=numpy.arange(0,math.pi*20,0.1)
    y_values=numpy.sin(x_values*B+C)                  #numpy.sin() 表示y值
    pylab.plot(x_values,y_values)                 #plot命令允许绘制二维线图
    pylab.xlabel('x axis')                      #x轴标签命名'x values'
    pylab.ylabel('y axis')                      #y轴标签命名'sin of x'
    pylab.title("sine curve")     #图表的题目
    pylab.grid(True)                              #图表添加一个网格
    pylab.show()                                  #展示图表
    
    
    
#to calculate the physiologic_index
#calculate_physiologic_index(year,month,day):#输入的年月日是生日
import leap_common_year,day_transformation,math,pylab,numpy

physiologic_index=0
dict_physiologic_index={}

def calculate_physiologic_index(year,month,day):#输入的年月日是生日
    B_emotion=(2*math.pi)/23
    B_physical=(2*math.pi)/28
    B_intelligence=(2*math.pi)/33
    
    birthday_number=day_transformation.total_day_calculate(year,month,day)
    
    initial_number_emotion=birthday_number%23    #initial_number是正弦函数起始值
    initial_number_physical=birthday_number%28
    initial_number_intelligence=birthday_number%33

    
    C_emotion=(-B_emotion)*initial_number_emotion
    C_physical=(-B_physical)*initial_number_physical
    C_intelligence=(-B_intelligence)*initial_number_intelligence

    x_values=numpy.arange(0,366,1)
    y_values_emotion=numpy.sin(x_values*B_emotion+C_emotion)    #numpy.sin() 表示y值
    y_values_physical=numpy.sin(x_values*B_physical+C_physical)
    y_values_intelligence=numpy.sin(x_values*B_intelligence+C_intelligence)

    # to calculate the physiologic_index
    for i in x_values:
        y_values_emotion=numpy.sin(i*B_emotion+C_emotion)    #numpy.sin() 表示y值
        y_values_physical=numpy.sin(i*B_physical+C_physical)
        y_values_intelligence=numpy.sin(i*B_intelligence+C_intelligence)
        physiologic_index=(y_values_emotion+y_values_physical+y_values_intelligence)/3
        dict_physiologic_index[i]=physiologic_index

    small_sorted_physiologic_index=sorted(dict_physiologic_index.items(),key=lambda d:d[1],reverse=False) #排序有小到大
    big_sorted_physiologic_index=sorted(dict_physiologic_index.items(),key=lambda d:d[1],reverse=True) #排序有小到大

    #print "small_sorted_physiologic_index is:",small_sorted_physiologic_index
    #print "big_sorted_physiologic_index is:",big_sorted_physiologic_index

    print "day of small values are:"
    i=0
    while i<10:
        #print big_sorted_physiologic_index[i]
        #print big_sorted_physiologic_index[i][0]
        #测试输出时间相对应的具体值
        #print small_sorted_physiologic_index[i]
        print day_transformation.number_to_time(year,small_sorted_physiologic_index[i][0])
        i+=1

    
    print "day of big values are:"
    i=0
    while i<10:
        print day_transformation.number_to_time(year,big_sorted_physiologic_index[i][0])
        i+=1

    

   
#leap year and common year

def leap_common_year(year):
    
    
    if year%100==0:
        if year%400==0:
            return "leap year"
       
        else:
            return "common year"
       
           
    elif year%4==0:
        return "leap year"
    
    else:
        return "common year"

