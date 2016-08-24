classifier分类器

分类器是一种计算机程序。

他的设计目标是在通过学习后，可自动将数据分到已知类别。

应用在搜索引擎以及各种检索程序中。同时也大量应于数据分析与预测领域。

分类器是一种机器学习程序，因此归为人工智能的范畴中。人工智能的多个领域，包括数据挖掘，专家系统，模式识别都用到此类程序。

对于分类器，其实质为数学模型。针对模型的不同，目前有多种分支，包括：Bayes分类器，BP神经网络分类器，决策树算法，SVM（支持向量机）算法等。

参考数据挖掘的各类文章，其中会对各种分类器算法的设计，性能，做出更为详细与准确的评价

 

 

回到正题，每个患者有11个值，患者ID，9个肿瘤的属性值和最终诊断。通过研究这些属性，找到肿瘤预测模式，根据肿瘤属性来判定肿瘤性质。对没见过面的患者（甚至不知道她的诊断结论），我们希望根据肿瘤的属性来判定是否为恶性肿瘤。为了实现，就要用分类器。分类器要使用已知类别样本进行训练。在训练过程中，分类器寻找指示分类（例如恶性或良性模式）。模式确定后，在已知的新样本数据上进行测试。在已知类别的样本上进行测试可以判定分类器准确性。

在此例中，诊断结果（良性或恶性）是对患者肿瘤属性的分类结果。每个患者信息都可以用于建立一个模式的内部模型，模式用于区分良性或恶性。训练好分类器后，必须要测试分类器效果。将数据分成两个部分，即分类器训练数据和测试数据。在实践中，创建两个单独的文件，大部分数据放入训练文件，剩余数据放入测试文件。

现在要解决问题是：如何编写从训练数据中发现分类模式的程序？

 

利用分治原理，每次查看患者的一个肿瘤属性，然后结合所属的类别意见作出决定。例如一个肿瘤厚度值范围1-10。较厚的肿瘤（例如大于7），可预测为恶性肿瘤，最后评估每个属性，得出判定结果，分类结果遵循遵循少数服从多数原理。

举例（1000025 ， 5,1,1,1,2,1,3,1,1） ，ID为1000025 的患者，先依次判定患者9个属性，分别为5,1,1,1,2,1,3,1,1 。总结患者9个属性，其中大部分都小于中值5，最后得出患者为良性肿瘤。

 

如何实现？对每个肿瘤属性设置两个平均值。第一个平均值是女性训练数据中，良性肿瘤患者平均值；第二个平均值是训练数据中，恶性肿瘤患者平均值。9个属性都训练后，应该得到18个平均值，即9个良性肿瘤平均值和9个恶性肿瘤平均值。

 

采用如下方法构造分类器：对每个属性的平均值，找出良性平均值和恶性平均值的中值。这个值就是分类值。分类器包括所有属性的分类值，即9个分类值。如果新样本的某个属性值低于该属性的分类值，预测为良性；反正为恶性。要得到整体的分类预测结果，需要将每个属性与该属性的分类值进行比较。根据属性值是大于或小于分类值对属性进行标记。在这例子中，小于分类值表示良性，大于分类值表示恶性。对于患者最后诊断，采用少数服从多数原则。9个属性中，占主导地位的类别即为患者的最终判定结果。

 

 

 

 

算法：

 变量多用复制粘贴，否则大小写很容易出错，不容易检查

将全部699个例患者数据分成两个文件，训练分类器文件和测试分类器文件。采用简单方法，349个患者数据用作训练数据，350个患者数据用作测试数据。 0代表缺失的统计数据，应该忽略含0的病人

（1）从训练文件中创建训练集trainingSet 

*打开文件

 

*初始化训练集为空

*对文件中每一行：将行内容解析成各组成部分

 为患者创建元组

 将元组添加到训练集列表中

 

（2）创建分类器classifier，使用训练集中确定每个属性的分类值

*函数参数是训练集。

*对每个训练集中的患者元组：

   如果元组代表良性肿瘤，则将每个患者属性添加到良性属性总和中，对良性肿瘤患者计数

   如果元组代表恶性肿瘤，则添加到恶性肿瘤属性总和中，对恶性肿瘤患者计数

   最后，得到18个总和，分别为每种良性肿瘤患者属性和恶性肿瘤患者属性的总和。同时得到良性患者和恶性患者数量。

*计算9个良性属性和9个恶性属性的平均值（总和/总人数）

*计算9个属性的良性平均值和恶性平均值的平均值。这个中值为分类值，是该属性属于良性还是恶性的诊断标准。这9个分类值构成分类器。

*trainClassifier要保存很多个人的总和和平均值。18个总和的平均值包含了很多变量，因此可用列表来进行管理。例如benignSums,benignAverage等列表。使用列表代替单个列表，需要编写代码来添加两个列表。因此需要多次求总和，所以利用函数完成此任务更容易，此外还需要总和列表计算平均值列表。由于需要多次计算平均值，因此将这部分分离出来用函数方式实现更好。两个函数分别为sumList和makeAverages.

 

sumList函数有两个参数，参数是两个同样大小的列表。函数返回一个新列表，该列表包含两个参数列表中元素的总和，也就是说第一个参数列表中的第一个元素和第二个参数列表的第一个元素相加，并将和作为求和列表中的第一个元素，以此类推。

创建listOfSums用于存放总和。使用乘法运算符创建列表，初始化为9个0，对列表而言，乘法是重复运算。创建变量index，在三个列表中用作索引。使用索引遍历参数列表，将相同索引的两个元素相加，结果放入listOfSums 中。

 

makeAverages和sumLists函数差别不大，参数为列表和总和值，将列表中的每个元素除以总和，并将计算结果作为列表返回。

 

 

 

 

（3）从测试文件中创建测试集 classifyTestSet

判断定分类器能否只根据患者的肿瘤属性，正确预测出诊断结果。这项测试由classifyTestSet 函数完成。该函数读入测试数据集（带有确诊断结果的患者肿瘤数据）。将患者的每个属性值与相应分类器值进行比较。如果该属性值大于分类器平均值，则认为该属性是恶性的证据。如果属性值小于分类器平均值，表明是良性。对每个患者的良性和恶性属性进行计数，然后采用少数服从多数规则。也就是说那种类型属性多，则预测为该类型。

 

 

（4）使用分类器（分类值），对测试集进行分类，同时计算这些判定的准确性

（5）数据结构：

（a）trainingSet 和testSet：包含每个患者的信息。患者数据是永远不会修改的，因此可以作为元组的值。所有患者数据构成元组列表。元组格式：第一项：患者ID，字符串类型；第二项：患者诊断结果，但字母字符串（单个字母‘m’，‘b’）;第三至十二项：肿瘤属性，按1-9顺序排列，整数类型。

(b)classifier:由9个不同值构成序列，因为这些值是不会改变的，所以构成元组，它包含9个浮点值，即每个良性平均值和恶性平均值的中值（两个平均值的中点）

（c）result：为元组列表

 

 

#生成训练数据集

def makeTrainingSet(fileName):

    tSet=[]

    trainingFile=open(fileName)

    for line in trainingFile:

        line=line.strip()

        if '0' in line:   #0代表缺失的统计数据，应该忽略含0的病人

            continue

        id,diag,a1,a2,a3,a4,a5,a6,a7,a8,a9=line.split(',')

        

        if diag=='4': #diagnosis is malignant

            diagMorB='m'

        else:

            diagMorB='b'

        patientTuple=(id,diagMorB,int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),\

                      int(a7),int(8),int(a9))

        tSet.append(patientTuple)

    return tSet

 

 

#求总和函数

def sumLists(list1,list2):

    '''element-by-element sums of lists of 9 items'''

    listOfSums=[0.0]*9    #注意0.0表示浮点数，否则python 2.7计算会出错

    for index in range(9):

        listOfSums[index]=list1[index]+list2[index]

    return listOfSums

 

 

 

 

#求平均数

def makeAverages(listOfSums,total):

    '''convert each list element into an average by dividing by the total'''

    averageList=[0.0]*9

    for index in range(9):

        averageList[index]=listOfSums[index]/float(total)

    return averageList

 

 

 

#用训练数据计算分类器

def trainClassifier(trainingSet):   

    '''build a classifier using the training set'''

    benignSums=[0]*9 #lists of sums of benign attributes

    benignCount=0  #count of benign patients

    malignantSums=[0]*9#lists of sums of malignant attributes

    malignantCount=0#count of malignant patients

    for patientTup in trainingSet:

        if patientTup[1]=='b': #if benign

            #add benign attributes to benign total

            benignSums=sumLists(benignSums,patientTup[2:])

            benignCount+=1

        else:

        #add malignant attributes to malignant total

            malignantSums=sumLists(malignantSums,patientTup[2:])

            malignantCount+=1

 

 

    benignAvgs=makeAverages(benignSums,benignCount)

    malignantAvgs=makeAverages(malignantSums,malignantCount)

 

    classifier=makeAverages(sumLists(benignAvgs,malignantAvgs),2)

    return classifier

        

 

 #分类器测试集

def classifyTestSet(testSet,classifier):

    results=[]

    #for each patient

    for patient in testSet:

        benignCount=0

        malignantCount=0

        #for each attribute of the patient

        for index in range(9):

            #if actual patient attribute is greater than separator value

            #note:the patient tuple has two extra element at the beginning

            #so we add 2 to each patient index to only index attributes

            if patient[index+2]>classifier[index]:

                #predict malignant for that attribute

                malignantCount+=1

            else:

                #predict benign for that attribute

                benignCount+=1

        #record patient id,both counts,and actual diganosis

        resultTuple=(patient[0],benignCount,malignantCount,patient[1])

        #add patient to list of result

        results.append(resultTuple)

    return results

 

 

 

 

#生成测试数据的报告，统计精确度

def reportResults(results):

    '''determine accuracy of classifier and report'''

    totalCount=0    #count of total number of results

    inaccurateCount=0#count of incorrect results

    inaccuracy_list=[]#存储不正确统计的ID号

 

    for r in results:

        totalCount+=1

        #if benignCount>malignantCount,we should predict'b'

        if r[1]>r[2]:

            if r[3]=='m': # this is the condition of inaccuracy

                inaccurateCount+=1 #if malignantCount>benignCount,we should predict 'm'

                inaccuracy_list.append(r[0])

        if r[1]<r[2]:

            if r[3]=='b':

                inaccurateCount+=1

                inaccuracy_list.append(r[0])

 

    print "of",totalCount,"patients,there were",inaccurateCount,'inaccuracies'

    print "the inaccurate ID are:",inaccuracy_list   #输出不准确的ID数据

 

 

            

 

 

 

#主函数

 

fileName='trainClassifierData.txt'

 

trainingSet=makeTrainingSet(fileName)

 

classifier=trainClassifier(trainingSet)

 

 

 

fileName1='testClassifierData.txt'

 

testSet=makeTrainingSet(fileName1)

 

results=classifyTestSet(testSet,classifier)

 

reportResults(results)
