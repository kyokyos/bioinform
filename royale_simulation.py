
#royale simulation.py 版本4，最新版本
#增加了捕食者的子类，进化类，拥有更强属性，程序模拟观察后，属性值较差的捕食者被自然法则淘汰，捕食者逐步而漫长进化，这个简单模拟器可以辅助证明达尔文适者生存法则。



import random,pylab


class Island():
    """Island,n*n grid where zero value indicates an unoccupied cell."""
    #生成一个n排，n列的点矩阵，矩阵是笛卡尔坐标系，x向右递增，y向上递增，（0,0）是左下角，（9,0）是右下角
    #（0,9）是左上角，（9,9）是右上角
    #程序输出顺序是从左上角（0,9）开始，（1,9），（2,9）。。。到右下角结尾（9,0）
    #岛上空白是数字0，在str显示时被‘.’取代
    
    def __init__(self,n,preyCnt=0,predatorCnt=0,advanced_predator_init=0):
        #print "in island init"
        self.gridSize=n
        self.grid=[]
        for i in range(n):   #生成一个点矩阵
            row=[0]*n #row is a list of zero
            self.grid.append(row)
        self.initAnimals(preyCnt,predatorCnt,advanced_predator_init)
        


    def __str__(self):
        """string representation for printing.
          (0,0)will be in the lower-left corner."""
        #print "in island str"
        s=""
        for j in range(self.gridSize-1,-1,-1): #print row size-1 first
            for i in range(self.gridSize):     #each row starts at 0
                if not self.grid[i][j]:
                    #print a '.' for empty space
                    s+="%-2s"%'.'+" "          # 字符串负号表示左对齐，这里表示左对齐2个单位
                else:
                    s+="%-2s"%(str(self.grid[i][j]))+" "

            s+="\n"

        return s

   

    def __repr__(self):
        return self.__str__()


    def __getitem__(self,a):
        #print "in getitem"
        #可以通过索引查看岛屿地域，还可以通过赋值语句让动物注册到岛上，更加人性化，比register方法更快 
        return self.grid[a]
        


    def register(self,animal):
        '''register animal with island, i.e.put it at the animal's coordinate'''
        #register函数是动物和岛屿交互的桥梁，动物的位置x,y被保存到岛屿笛卡尔坐标系中
        #print "in island register"
        x=animal.x
        y=animal.y

        self.grid[x][y]=animal

    def size(self):
        '''reture the size of island:one dimension'''
        #print "in island size"
        return self.gridSize


    def animal(self,x,y):
        #print "in animal check"
        #查看岛屿某位置是否有Animal实例
        if 0<=x<self.gridSize and 0<=y<self.gridSize:
            #print "ok"
            return self.grid[x][y]
        else:
            #print "no"
            return -1 #outside the land boundary


    def initAnimals(self,preyCnt,predatorCnt,advanced_predator_init):
        '''put some initial animals on the island'''
        #猎物初始化
        cnt=0
        #while loop continues until preyCnt unoccupied positions are found
        while cnt<preyCnt:
            x=random.randint(0,self.gridSize-1)
            y=random.randint(0,self.gridSize-1)
            if self[x][y]==0:   #if not self.animal(x,y):
                newPrey=Prey(island=self,x=x,y=y)
                cnt+=1
                self.register(newPrey)

        #捕食者初始化
        cnt=0
        while cnt<predatorCnt:
            x=random.randint(0,self.gridSize-1)
            y=random.randint(0,self.gridSize-1)
            if self[x][y]==0:   #if not self.animal(x,y):
                newPred=Predator(island=self,x=x,y=y)
                cnt+=1
                self.register(newPred)

        #高级捕食者初始化
        cnt=0
        while cnt<advanced_predator_init:
            x=random.randint(0,self.gridSize-1)
            y=random.randint(0,self.gridSize-1)
            if self[x][y]==0:   #if not self.animal(x,y):
                new_advanced_Predator=Advanced_Predator(island=self,x=x,y=y)
                cnt+=1
                self.register(new_advanced_Predator)
            
   


    def remove(self,animal):
        x=animal.x        
        y=animal.y
        self.grid[x][y]=0


    def clearAllMovedFlags(self):
        '''Animals have a moved flag to indicated that they moved this turn.clear
         that we can do next turn动物已经移动旗帜来表示它们在此循环中移动。
        清除网格所有动物旗帜，让它们能在下一轮中移动'''

        for x in range(self.gridSize):
            for y in range(self.gridSize):
                if self.grid[x][y]:
                    self.grid[x][y].clearMovedFlag()

    def preyCount(self):
        '''count all the prey on the island岛屿猎物统计'''
        cnt=0
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                animal=self.animal(x,y)
                if animal:
                    if isinstance(animal,Prey):
                        cnt+=1
        return cnt

    def predatorCount(self):
        '''count all the predators on the island岛屿捕食者统计'''
        cnt=0
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                animal=self.animal(x,y)
                if animal:
                    if isinstance(animal,Predator):
                        cnt+=1
        return cnt

    def advanced_predatorCount(self):
        cnt=0
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                animal=self.animal(x,y)
                if animal:
                    if isinstance(animal,Advanced_Predator):
                        cnt+=1
        return cnt
        



        


    def equilibrium(self):
        #大自然通过疾病，瘟疫，极端气候和其它因素控制某种族的数量，阻止其无限制发展
        
        size=self.gridSize
        total_numbers=size**2
        preyCnt = self.preyCount()
        predCnt = self.predatorCount()

        #如果猎物繁殖数量超过岛屿百分之60，则启动平衡机制
        if preyCnt/float(total_numbers)>0.6:
            print"in prey equilibrium"
            before_remove_prey_numbers=preyCnt/2 #需要移除的猎物数量
            after_remove_prey_cnt=0  #统计核实移除数量是否正确

         
            for x in range(size):
                for y in range(size):
                    animal = self.animal(x,y)
                    if animal:                      #如果是动物
                        if isinstance(animal,Prey): #如果动物是捕食者，则运行eat（）方法
                            animal.island.remove(animal)#移除猎物
                            before_remove_prey_numbers-=1
                            after_remove_prey_cnt+=1
                            
                if before_remove_prey_numbers<=0:
                    print "nature has removed:%d"%(after_remove_prey_cnt)
                    break   #有问题,数字不准确，移除是大概值，这里可以解释为随机性或不可预测造成
                    

        #如果捕食者数量超过猎物五分之一，则采用平衡机制
        if predCnt/float(preyCnt)>0.3:
            print"in predator equilibrium"
            before_remove_pred_numbers=predCnt/3
            print "before remove_pred_numbers:%d"%(before_remove_pred_numbers)
            after_remove_pred_cnt=0  #统计核实移除数量是否正确

            for x in range(size):
                for y in range(size):
                    animal = self.animal(x,y)
                    if animal:                      #如果是动物
                        if isinstance(animal,Predator): #如果动物是捕食者，则运行eat（）方法
                            animal.island.remove(animal)#移除猎物
                            print "remove predator"
                            before_remove_pred_numbers-=1
                            after_remove_pred_cnt+=1
                if before_remove_pred_numbers<=0:
                    print "nature has removed:%d"%(after_remove_pred_cnt)
                    break   #有问题，数字不准确，移除是大概值,这里可以解释为随机性或不可预测造成
                
                
                
                                
                                
                                
                


class Animal(object):
    
    def __init__(self,island,x=0,y=0,name="A"):
        '''initialize the animal's name and their position'''
        #print "in animal init"
        #x和y的值表示岛上的动物将被放置的位置。
        #Animal实例还需要知道它位于哪个岛屿
        #最后需要它的名字：moose或wolf
        self.island=island
        self.name=name
        self.x=x
        self.y=y
        self.moved=False  #设置为静止，即未移动状态
        self.clockTicked=False #生物钟递减为否


    def __str__(self):
        #print "in animal str"
        return self.name


    def __repr__(self):
        #print "in animal repr"
        return self.__str__()


    def position(self):
        '''return the coordinates of current position'''
        #print 'in animal position'
        return self.x, self.y


    def checkGrid(self,typeLookingFor=int):
        '''look in the 8 direction from the animal's location and return the first
        location that presently has an object of the specified type.return 0 if
        no such location exists'''
        #eat(),move()函数都会用到checkGrid()，把此函数改为随机性
        

        # neighbor offsets
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)] 
        result = 0
        for i in range(len(offset)*8):
            random_move=random.randint(0,len(offset)-1)
            x=self.x+offset[random_move][0]
            y=self.y+offset[random_move][1]
            if not 0 <= x < self.island.size() or \
               not 0 <= y < self.island.size():
                continue
            
 
            if type(self.island.animal(x,y))==typeLookingFor:
                #print "found target" 
                result=(x,y)
                break
           
        return result

    def move(self):
        '''Move to an open, neighboring position移动到旁边一个空位置 '''
        if not self.moved: #如果未移动，则下面程序执行
            location = self.checkGrid(int)  #寻找空白地
            if location:
                # print 'Move, %s, from %d,%d to %d,%d'% \
                #       (type(self),self.x,self.y,location[0],location[1])
                self.island.remove(self)  # remove from current spot
                self.x = location[0]  # new coordinates
                self.y = location[1]
                self.island.register(self) # register new coordinates
                self.moved=True     #移动标记设置为真，则移动后不会再次移动
               
    
  


    def breed(self):
        '''breed a new Animal,if there is room in one of the 8 locations, place the
        new prey there.otherwise,you have to wait'''
        if self.breedClock<=0:
            location=self.checkGrid(int)
            if location:
                self.breedClock=self.breedTime
                #print"self.breedClock now return to:",self.breedClock
                theClass=self.__class__
                newAnimal=theClass(self.island,x=location[0],y=location[1])
                self.island.register(newAnimal)


    def clearMovedFlag(self):
        #让动物移动设置为False，方便下次移动
        self.moved=False
        self.clockTicked=False

  
   
            
    
class Prey(Animal):
    #每个实例都有自己时钟，用于跟踪繁殖时间。predator还有第二个时钟，用于跟踪挨饿时间。也就是
    #说，创建实例需要初始化内部“时钟”。每个实例通过clockTick方法，在每个时排，更新自己的时钟。当他们
    #繁殖时钟计数到0时，他们能繁殖。饥饿时钟同理
    def __init__(self,island,x=0,y=0,s="O"):
        #print"in prey init"
        Animal.__init__(self,island,x,y,s)
        self.breedClock=self.breedTime #breedClock是时钟，会变化，所以用另一个变量名

    def clockTick(self):
        '''prey updates only its local breed clock'''
        if self.clockTicked==False:
            
            self.breedClock-=1
            self.clockTicked=True
            
        
        


class Predator(Animal):
    def __init__(self,island,x=0,y=0,s="X"):
        #print "in predator init"
        Animal.__init__(self,island,x,y,s)
        self.breedClock=self.breedTime
        self.starveClock=self.starveTime



    def move(self):
        if not self.moved: #如果未移动，则下面程序执行
            offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)] 
            result = 0
            for i in range(len(offset)*8):
                random_move=random.randint(0,len(offset)-1)
                x=self.x+offset[random_move][0]
                y=self.y+offset[random_move][1]

                #如果x,y超过取值范围，则重新循环           
                if not 0 <= x < self.island.size() or \
                   not 0 <= y < self.island.size():
                    continue
            
                #如果目的地是空地，则移动
                if type(self.island.animal(x,y))==int: 
                    self.island.remove(self)  # remove from current spot
                    self.x =x                 # new coordinates
                    self.y =y
                    self.island.register(self) # register new coordinates
                    self.moved=True     #移动标记设置为真，则移动后不会再次移动
                    break
                
                #如果目的地是猎物，则进食
                if type(self.island.animal(x,y))==Prey: 
                    self.island.remove(self.island.animal(x,y))#删除location上的prey
                    self.island.remove(self)  # remove from current spot
                    self.x =x                 # new coordinates
                    self.y =y
                    self.island.register(self)#捕食者注册到猎物位置上
                    self.starveClock=self.starveTime
                    self.moved=True     #移动标记设置为真，则移动后不会再次移动
                    break

                #如果目的地居住有同伴，则重新移动
                if type(self.island.animal(x,y))==Predator:
                    continue

    def eat(self):
        '''predator looks for one of the eight locations with Prey,if found,moves to that location,
     updates the starve clock,removes the Prey'''
        if not self.moved and self.starveClock<=1:
            print "in eat"
            location=self.checkGrid(Prey)
            if location:
                self.island.remove(self.island.animal(location[0],location[1])) #删除location上的prey
                self.island.remove(self)#清空捕食者现在位置
                self.x=location[0]
                self.y=location[1]
                self.island.register(self)#捕食者注册到猎物位置上
                self.starveClock=self.starveTime
                self.moved=True #行为结束后移动设置为True，不会再次移动


    def clockTick(self):
        #每经历一次事件循环，都需要更新每个实例的当前状态，特别是初始化为类值（繁殖和挨饿时间）的那些个体的时钟必须递减。因此，每
        #个类需要一个方法来在每个时钟节拍内更新内部实例的时钟。在每个子类中创建了两个方法，叫clockTick
        if self.clockTicked==False:
            self.breedClock-=1
            self.starveClock-=1
            self.clockTicked==True
            
        if self.starveClock<=0:
            self.island.remove(self)
                    


               

    def clockTick(self):
        #每经历一次事件循环，都需要更新每个实例的当前状态，特别是初始化为类值（繁殖和挨饿时间）的那些个体的时钟必须递减。因此，每
        #个类需要一个方法来在每个时钟节拍内更新内部实例的时钟。在每个子类中创建了两个方法，叫clockTick
        if self.clockTicked==False:
            self.breedClock-=1
            self.starveClock-=1
            #print "self.starveClock:",self.starveClock
            self.clockTicked=True
            
            
        if self.starveClock<=0:
            self.island.remove(self)
            


class Advanced_Predator(Predator):
    def __init__(self,island,x=0,y=0,s="W"):
        Predator.__init__(self,island,x,y,s)
        self.breedClock=self.breedTime-2
        self.starveClock=self.starveTime+2


    def eat(self):
        #高级版本捕食者具有自动探测猎物能力
        if not self.moved:  
            location=self.checkGrid(Prey)
            if location:
                self.island.remove(self.island.animal(location[0],location[1])) #删除location上的prey
                self.island.remove(self)#清空捕食者现在位置
                self.x=location[0]
                self.y=location[1]
                self.island.register(self)#捕食者注册到猎物位置上
                self.starveClock=self.starveTime
                self.moved=True #行为结束后移动设置为True，不会再次移动



def main(predBreed=6,predStarve=4,predInit=10,preyBreed=5,preyInit=50,size=15,\
         ticks=300,advanced_predator_init=3):
    '''main simulation;sets defaults,runs event loop,plots at the end'''
    #initialization of the simulation
    #添加main函数来初始化模型和用循环以驱动模拟。下面是循环驱动的框架
    #1.创建Island实例和一些Predator实例和Prey实例
    #2.在指定数量的时间周期内进行循环
    #   2.1移动每个实例
    
    #predBreed:Predator实例繁殖前必须经过的时间间隔
    #preyBreed：Prey实例繁殖前必须经过的时间间隔
    #predStarve: Predator实例必须在此时间间隔中进食，否则会饿死
    #preInit:最初放入岛上的Predator实例个数
    #preyInit:最初放入岛上的prey实例个数
    #Size： Island实例一边的长度（假设岛是一个正方形）
    #ticks: 模拟结束前将经过的时间间隔数目

    #initialization values
    Predator.breedTime=predBreed
    Predator.starveTime=predStarve
    Prey.breedTime=preyBreed

    # for graphing 用于绘图
    predList=[]  #每一个时钟捕食者数量将放入此列表
    advanced_predList=[]#每一个时钟高级捕食者数量将放入此列表
    preyList=[]  #每一个时钟猎物数量将放入此列表

    #make an island
    
    isle=Island(size,preyInit,predInit,advanced_predator_init)
    print "initial prey num:%d,inital predator num:%d,inital advanced_predator num:%d,"%(preyInit,predInit,advanced_predator_init)
    print "init isle:"
    print isle
    
    


    #event loop
    #for all the ticks,for every x,y location
    #if there is an animal there,try eat,move,breed and clockTick
    
    for i in range(ticks):
        print "tick%d:"%(i)
        #大自然平衡自检
        isle.equilibrium()
        
        #import to clear all the moved flags!记得清楚所有标记，让moved=False
        isle.clearAllMovedFlags()
        for x in range(size):
            for y in range(size):
                animal=isle.animal(x,y)
                if animal:
                    if isinstance(animal,Predator): #如果动物是捕食者，则运行eat（）方法
                        animal.eat()
                    animal.move()    #动物移动
                    animal.breed()   #动物繁殖
                    animal.clockTick() #动物生物钟递减1，如果捕食者饥饿时钟<0，
                                      #则饿死，从岛上注销
        
        print isle
        #record info for display,plotting
        preyCnt=isle.preyCount()
        predCnt=isle.predatorCount()
        Advanced_predCnt=isle.advanced_predatorCount()
        print "prey num:%d,predator num:%d,advanced_pred num:%d"%(preyCnt,predCnt,Advanced_predCnt)
        

        if preyCnt==0:
            print 'lost the Prey population,quiting'
            break

        if predCnt==0:
            print 'lost the Predator population,quiting'
            break

        preyList.append(preyCnt)
        predList.append(predCnt)
        advanced_predList.append(Advanced_predCnt)
        #print out every 10th cycle,see what’s going on
        if not i%10:
            print preyCnt,predCnt,Advanced_predCnt
            #print 'preyCnt num:',preyCnt
            #print 'predCnt num:',predCnt
            #print '*'*20
            #print isle

    pylab.plot(predList,'r')
    pylab.plot(preyList,'b')
    pylab.plot(advanced_predList,'y')
    pylab.title('predator(red),advanced_predList(yellow), and prey(blue) simulation')
    pylab.xlabel('time ticks')
    pylab.ylabel('numbers')
    pylab.show()
        



def isle_test():
    
    k=10
    grid=[]
    S=''
    for i in range(k):
        row=[0]*k
        grid.append(row)


    print grid

    for j in range(k-1,-1,-1):
        for i in range(k):
            if not grid[i][j]:
                print 'yes'
                S+="%-2s"%'.'+''
                print S
            else:
                print 'no'
                S+=""%(str(grid[i][j]))
                print S
            print "grid[%d][%d] is:" %(i,j),grid[i][j]
        S+="\n"




     

def move_test(predBreed=6,predStarve=6,predInit=10,preyBreed=3,preyInit=30,size=10,\
         ticks=20):
  
    Prey.breedTime=preyBreed
    Predator.breedTime = predBreed
    Predator.starveTime = predStarve
    
    #make an island
    isle=Island(size,preyInit,predInit)
    print "init isle:"
    print isle

    
    for i in range(ticks):
        print "tick%d:"%(i) 
        #import to clear all the moved flags!记得清楚所有标记，让moved=False
        isle.clearAllMovedFlags()
        for x in range(size):
            for y in range(size):
                #print "x,y:",x,y 主函数遍历测试
                animal=isle.animal(x,y)
                if animal:
                    animal.move()    #动物移动
                    animal.clockTick()
                    #print"breedClock:",animal.breedClock
        preyCnt=isle.preyCount()
        predCnt=isle.predatorCount()
        print "prey num:%d,predator num:%d"%(preyCnt,predCnt)               
        print isle
        

        
def breed_test(predBreed=500,predStarve=500,predInit=0,preyBreed=3,preyInit=1,size=10,\
         ticks=10):
    #测试成功，纠正了两位教授代码
    #Predator.breedTime=predBreed
    #Predator.starveTime=predStarve
    Prey.breedTime=preyBreed


    #make an island
    isle=Island(size,preyInit,predInit)
    print "initial prey num:%d,predator num:%d"%(preyInit,predInit)
    print "init isle:"
    print isle
    
    
    for i in range(ticks):
        print "tick%d:"%(i)
        
        #import to clear all the moved flags!记得清楚所有标记，让moved=False
        isle.clearAllMovedFlags()
        for x in range(size):
            for y in range(size):
                animal=isle.animal(x,y)
                if animal:
                    animal.move()
                    animal.breed()   #动物繁殖
                    animal.clockTick() #动物生物钟递减1，如果捕食者饥饿时钟<0，#则饿死，从岛上注销
                    print"breedClock:",animal.breedClock
        preyCnt=isle.preyCount()
        predCnt=isle.predatorCount()
        print "prey num:%d,predator num:%d"%(preyCnt,predCnt)
        print isle
        
        
def starve_test(predBreed=6,predStarve=3,predInit=3,preyBreed=3,preyInit=0,size=10,\
         ticks=10):
    Predator.breedTime=predBreed
    Predator.starveTime=predStarve
    Prey.breedTime=preyBreed
    isle=Island(size,preyInit,predInit)
    print "initial prey num:%d,inital predator num:%d"%(preyInit,predInit)
    print "init isle:"
    print isle
    for i in range(ticks):
        print "tick%d:"%(i)
        
        #import to clear all the moved flags!记得清楚所有标记，让moved=False
        isle.clearAllMovedFlags()
        for x in range(size):
            for y in range(size):
                animal=isle.animal(x,y)
                if animal:
                    if isinstance(animal,Predator):
                        animal.eat() #如果是捕食者，进食
                    animal.move()    #动物移动
                    animal.breed()   #动物繁殖
                    animal.clockTick() #动物生物钟递减1，如果捕食者饥饿时钟<0，
                                      #则饿死，从岛上注销
        
        print isle
        #record info for display,plotting
        preyCnt=isle.preyCount()
        predCnt=isle.predatorCount()
        print "prey num:%d,predator num:%d"%(preyCnt,predCnt)


def eat_test(predBreed=6,predStarve=3,predInit=1,preyBreed=3,preyInit=99,size=10,\
         ticks=10):
    Predator.breedTime=predBreed
    Predator.starveTime=predStarve
    Prey.breedTime=preyBreed
    isle=Island(size,preyInit,predInit)
    print "initial prey num:%d,inital predator num:%d"%(preyInit,predInit)
    print "init isle:"
    print isle
    for i in range(ticks):
        print "tick%d:"%(i)
        
        #import to clear all the moved flags!记得清楚所有标记，让moved=False
        isle.clearAllMovedFlags()
        for x in range(size):
            for y in range(size):
                animal=isle.animal(x,y)
                if animal:
                    if isinstance(animal,Predator):
                        animal.eat() #如果是捕食者，进食
                    animal.move()    #动物移动
                    animal.breed()   #动物繁殖
                    animal.clockTick() #动物生物钟递减1，如果捕食者饥饿时钟<0，
                                      #则饿死，从岛上注销
        
        print isle
        #record info for display,plotting
        preyCnt=isle.preyCount()
        predCnt=isle.predatorCount()
        print "prey num:%d,predator num:%d"%(preyCnt,predCnt)
