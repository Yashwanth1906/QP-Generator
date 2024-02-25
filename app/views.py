import random
from django.shortcuts import render,redirect
from .models import questions,partA,partC,partB,Image
from .forms import ImageForm,wordreaderform
import csv
import io
# Create your views here.

code = ""
branch = ""
set = ""
date = ""
year = ""
semester = ""
assessment = ""
def showindex(r):
    global code,set,branch,date,year,semester,assessment
    partA.objects.all().delete()
    partB.objects.all().delete()
    partC.objects.all().delete()
    if r.method == "POST":
        parta_diff1 = r.POST.get('partA_diff1')
        parta_diff2 = r.POST.get('partA_diff2')
        parta_diff3 = r.POST.get('partA_diff3')
        partb_diff1 = r.POST.get('partB_diff1')
        partb_diff2 = r.POST.get('partB_diff2')
        partb_diff3 = r.POST.get('partB_diff3')
        code = r.POST.get('subject_code')
        branch = r.POST.get('branch')
        set = r.POST.get('set')
        date = r.POST.get('date')
        year = r.POST.get('year')
        semester = r.POST.get('semester')
        assessment = r.POST.get('assestype')
        partA.objects.create(difficulty1 = parta_diff1,difficulty2 = parta_diff2,difficulty3 = parta_diff3)
        partB.objects.create(difficulty1 = partb_diff1,difficulty2 = partb_diff2,difficulty3 = partb_diff3)
    return render(r,"tab2.html")
parta_questions = []
partb_questions = []
partc_questions = []
message = ""
counta = 1
check1 = []
for i in range(5):
    check1.append(i)
print(check1)
def parta_generateqns(x,diff):    # x is the the difficulty level and diff is the no.of.questions in that
    y = questions.objects.all()     #getting all the questions
    qn = y.values('question','Type','difficulty','marks')
    questions1 = []              #organising all the questions in this list
    for i in qn:
        temp = []
        temp.append(i['question'])
        temp.append(i['Type'])
        temp.append(i['difficulty'])
        temp.append(i['marks'])
        questions1.append(temp)     
    count = 0
    global message
    for i in questions1:
        if i[2] == x:
            count+=1
    if count ==0:   # no questioins found in that difficulty level
        message += "no questions found in diffculty"+str(x)+"in parta,"    
        return
    if count<diff:    # setting to the no.of.questions to available no.of.questions
        diff = count
        message += "only found "+str(count)+" questions in difficulty"+str(x)+" in parta,"
    count = 0
    taken = []
    while(True):
        selected = random.choice(questions1)
        if selected[2]==x and selected[3] ==2:
            global counta
            temp =  selected[0]
            if temp not in taken:
                parta_questions.append(temp)
                taken.append(temp)
                count+=1
                counta+=1
            if count == diff:
                break
taken = []
def partb_generateqns(x,diff,part):
    y = questions.objects.all()
    qn = y.values('question','Type','difficulty','marks')
    questions1 = []
    for i in qn:
        temp = []
        temp.append(i['question'])
        temp.append(i['Type'])
        temp.append(i['difficulty'])
        temp.append(i['marks'])
        questions1.append(temp)
    global message
    count = 0
    tens = 0
    sixs = 0
    eights = 0
    fours = 0
    twelves = 0
    sixteens = 0
    for i in questions1:
        if i[1] == part and i[2] == x and len(i)>=4 and i not in taken:
            if i[3] == 10:
                tens+=1
            elif i[3] == 6:
                sixs +=1
            elif i[3] == 8:
                eights +=1
            elif i[3] == 4:
                fours += 1
            elif i[3] == 12:
                twelves += 1
            elif i[3] == 16:
                sixteens+=1
    check = min(tens,sixs) + min(fours,twelves) + (eights//2) + sixteens
    if check == 0:
        message += "no questions found in partb in difficulty"+str(x)
        return
    if check < diff:
        diff = check
        message += "Only "+str(check)+" questions in difficulty"+str(x)+","
    while(True):
        qn = random.choice(questions1)
        if (qn[1] == part) and qn[2] == x and len(qn)>=4 and qn not in taken:
            if qn[3] == 16:
                partb_questions.append(qn)
                questions1.remove(qn)
                count+=1
            elif qn[3] == 8:
                c = 0
                for i in questions1:
                    if len(i)>=4 and i[3] == 8 and i[1] == part and i[2] == x and i not in taken:
                        c+=1
                if c>1:
                    temp = []
                    temp.append(qn)
                    questions1.remove(qn)
                    while True:
                        another = random.choice(questions1)
                        if len(another)>=4 and another[3] == 8 and another[1] == part and another[2] == x and another not in taken:
                            temp.append(another)
                            questions1.remove(another)
                            count+=1
                            partb_questions.append(temp)
                            break
            elif qn[3] == 12:
                c = 0
                for i in questions1:
                    if len(i)>=4 and i[3] == 4 and i[1] == part and i[2] == x and i not in taken:
                        c+=1
                if c>0:
                    temp = []
                    temp.append(qn)
                    questions1.remove(qn)
                    while True:
                        another = random.choice(questions1)
                        if len(another)>=4 and another[3] == 4 and another[1] == part and another[2] == x and another not in taken:
                            temp.append(another)
                            questions1.remove(another)
                            partb_questions.append(temp)
                            count+=1
                            break
            elif qn[3] == 10:
                c = 0
                for i in questions1:
                    if len(i)>=4 and i[3] == 6 and i[1] == part and i[2] == x and i not in taken:
                        c+=1
                if c>0:
                    temp =[]
                    temp.append(qn)
                    questions1.remove(qn)
                    while True:
                        another = random.choice(questions1)
                        if len(another)>=4 and another[3] == 6 and another[1] == part and another[2] == x and another not in taken:
                            temp.append(another)
                            taken.append(another)
                            questions1.remove(another)
                            count+=1
                            partb_questions.append(temp)
                            break
        if count == diff:
            break
def showqns(r):
    global code,set,branch,date,year,semester,assessment
    parta = partA.objects.values('difficulty1','difficulty2','difficulty3')  #getting the no.of.questions in the difficulty level
    partb = partB.objects.values('difficulty1','difficulty2','difficulty3')
    parta_diff1 = parta[0]['difficulty1']
    parta_diff2 = parta[0]['difficulty2']
    parta_diff3 = parta[0]['difficulty3']
    partb_diff1 = partb[0]['difficulty1']
    partb_diff2 = partb[0]['difficulty2']
    partb_diff3 = partb[0]['difficulty3']
    f = questions.objects.all()
    qn = f.values('question','Type','difficulty','marks','topic')
    questions1 = []
    for i in qn:
        temp = []
        temp.append(i['question'])
        temp.append(i['Type'])
        temp.append(i['difficulty'])
        temp.append(i['marks'])
        temp.append(i['topic'])
        questions1.append(temp)
    topics = []
    for i in questions1:
        if i[4] not in topics:
            topics.append(i[4])
    print(topics)
    x = []
    for i in range(len(topics)):
        temp = []
        x.append(temp)
    print(x)
    for k,j in enumerate(topics):
        for i in questions1:
            if j == i[4]:
                x[k].append(i)
    solveA("a",1,parta_diff1,x)
    solveA("a",2,parta_diff2,x)
    solveA("a",3,parta_diff3,x)
    partb_generateqns(1,partb_diff1,'b')
    partb_generateqns(2,partb_diff2,'b')
    partb_generateqns(3,partb_diff3,'b')
    global message
    global counta
    global questiona_paper
    global partb_questions
    z = partb_questions
    partaqns= []
    for i in questiona_paper:
        partaqns.append(i[0])
    y = message
    partb_questions = []
    questiona_paper = []
    a11 = []
    b11 = []
    a12  =[]
    b12 = []
    a13  =[]
    b13 = []
    a14  =[]
    b14 = []
    a15  =[]
    b15 = []
    no = 0
    for i in z:
        print(i)
    for i in z:
        if len(i)==4:
            if no == 0:
                a11.append(i[0])
                no+=1
                continue
            elif no == 1:
                b11.append(i[0])
                no+=1
            elif no == 2:
                a12.append(i[0])
                no+=1
            elif no == 3:
                b12.append(i[0])
                no+=1
            elif no == 4:
                a13.append(i[0])
                no+=1
            elif no == 5:
                b13.append(i[0])
                no+=1
            elif no == 6:
                a14.append(i[0])
                no+=1
            elif no == 7:
                b14.append(i[0])
                no+=1
            elif no == 8:
                a15.append(i[0])
                no+=1
            elif no == 9:
                b15.append(i[0])
                no+=1
            else:
                break
        elif len(i)>4:
            for j in i:
                if no == 0:
                    a11.append(j[0])
                elif no == 1:
                    b11.append(j[0])
                elif no == 2:
                    a12.append(j[0])
                elif no == 3:
                    b12.append(j[0])
                elif no == 4:
                    a13.append(j[0])
                elif no == 5:
                    b13.append(j[0])
                elif no == 6:
                    a14.append(j[0])
                elif no == 7:
                    b14.append(j[0])
                elif no == 8:
                    a15.append(j[0])
                elif no == 9:
                    b15.append(j[0])
                else:
                    break
            no+=1
    print(taken)
    print("a11:",end="")
    print(a11)
    print("b11:",end="")
    print(b11)
    message = ""
    counta = 1
    return render(r,"show.html",{'parta':partaqns,'message':y,'partb':z,'a':code,'b':set,'c':branch,'d':date,'e':year,'f':semester,'g':assessment,'11a':a11,'11b':b11,'12a':a12,'12b':b12,'13a':a13,'13b':b13,'14a':a14,'14b':b14,'15a':a15,'15b':a15})

def showimage(r):
    if r.POST:
        x = ImageForm(r.POST)
        x.save()
        y = Image.objects.all()
        print(y)
        return render(r,"image.html",{'image':y})
    else:
        z= ImageForm()
        return render(r,"image.html",{'values':z})
    
def showupload(r):
    msg = ''
    if r.POST:
        csv_file = r.FILES['word_upload']
        if csv_file:
            file_content = csv_file.read()
            try:
                decode_content = file_content.decode("utf-8")
            except:
                decode_content = file_content.decode("utf-8",errors = 'replace')
            file = io.StringIO(decode_content,newline=None)
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for i in csv_reader:
                try:
                    questions.objects.create(   
                        sno = i[0],
                        question = i[1],
                        answer = i[2],
                        Type = i[3],
                        difficulty = i[4],
                        BT = i[5],
                        CO =i[6],
                        marks = i[7],
                        topic = i[8])
                except Exception as e:
                    msg += f"An unexpected error occurred during the upload process:{e}"
            f = questions.objects.all()
            qn = f.values('question','Type','difficulty','marks','topic')
            questions1 = []
            for i in qn:
                temp = []
                temp.append(i['question'])
                temp.append(i['Type'])
                temp.append(i['difficulty'])
                temp.append(i['marks'])
                temp.append(i['topic'])
                questions1.append(temp)
            topics = []
            for i in questions1:
                if i[4] not in topics:
                    topics.append(i[4])
            print(topics)
            x = []
            for i in range(len(topics)):
                temp = []
                x.append(temp)
            print(x)
            for k,j in enumerate(topics):
                for i in questions1:
                    if j == i[4]:
                        x[k].append(i)
    y = wordreaderform()
    return render(r,"upload.html",{'form':y,'message':msg})
def truncate(r):
    questions.objects.all().delete()
    return render(r,"exit.html")

def showrandom(r):
    y = questions.objects.all()
    qn = y.values('question','Type','difficulty','marks','topic')
    questions1 = []
    for i in qn:
        temp = []
        temp.append(i['question'])
        temp.append(i['Type'])
        temp.append(i['difficulty'])
        temp.append(i['marks'])
        temp.append(i['topic'])
        questions1.append(temp)
    print(questions1)
    parta = []
    count = 0
    for i in questions1:
        if i[3] == 2:
            count+=1
    if count >=5:
        num = 5
    else:
        num = count
    count = 0
    while True:
        qn = random.choice(questions1)
        if(qn[3]==2):
            parta.append(qn)
            questions1.remove(qn)
            count += 1
            if count == num:
                break
    print(parta)
    print(questions1)
    partb = []
    count = 0
    tens = 0
    sixs = 0
    eights = 0
    fours = 0
    twelves = 0
    sixteens = 0
    for i in questions1:
        if i[3] == 10:
            tens+=1
        elif i[3] == 6:
            sixs +=1
        elif i[3] == 8:
            eights +=1
        elif i[3] == 4:
            fours += 1
        elif i[3] == 12:
            twelves += 1
        elif i[3] == 16:
            sixteens+=1
    check = min(tens,sixs) + min(fours,twelves) + (eights//2) + sixteens
    if check>=5:
        num = 5
    else:
        num = check
    while(True):
        qn = random.choice(questions1)
        if qn[3] == 16:
            partb.append(qn)
            questions1.remove(qn)
            count+=1
        elif qn[3] == 8:
            c = 0
            for i in questions1:
                if  i[3] == 8:
                    c+=1
                if c>1:
                    partb.append(qn)
                    while True:
                        another = random.choice(questions1)
                        if another[3] == 8:
                            partb.append(another)
                            questions1.remove(another)
                            count+=1
                            break
        elif qn[3] == 12:
            c = 0
            for i in questions1:
                if len(i)>=4 and i[3]:
                    c+=1
                if c>0:
                    partb.append(qn)
                    questions1.remove(qn)
                    while True:
                        another = random.choice(questions1)
                        if len(another)>=4 and another[3] == 4:
                            partb.append(another)
                            questions1.append(another)
                            count+=1
                            break
        elif qn[3] == 10:
            c = 0
            for i in questions1:
                if len(i)>=4 and i[3] == 6:
                    c+=1
                if c>0:
                    partb.append(qn)
                    questions1.remove(qn)
                    while True:
                        another = random.choice(questions1)
                        if len(another)>=4 and another[3] == 6:
                            partb.append(another)
                            questions1.remove(another)
                            count+=1
                            break
        if count == num:
            break
    print("parta")
    print(parta)
    print("partb")
    print(partb)
    return render(r,"show.html",{'parta':parta,'partb':partb})

def call(topics,li,part,diff,questions):
    for i in range(topics):
        for j in questions[i]:
            if (j[1]==part) and (j[2]==diff):
                li[i]=1
                break
questiona_paper = []
def solveA(part,diff,num,questions):
    global questiona_paper
    check = 0
    topics = 0
    for i in questions:
        topics+=1                         
        for j in i:                       
            if j[1]==part and j[2]==diff: 
                check+=1
    if check < num:
        num = check

    li = [0]*topics
    call(topics,li,part,diff,questions)
    count = 0
    while(True):
        if (num==0):
            break
        topic = random.choice(questions)
        question = random.choice(topic)
        if (question[1]==part) and (question[2]==diff) and li[questions.index(topic)]==1:
            #print("{}.) {} (2x1=2)".format(count+1,question[0]))
            questiona_paper.append(question)
            topic.remove(question)
            count += 1
            li[questions.index(topic)]=0
            if count == num:
                break
            if li.count(0)==len(li):
                #li=[0]*topics
                call(topics,li,part,diff,questions)
    print(questiona_paper)

def call2(temp,q_p_t):
    for i in range(len(q_p_t)):
        if q_p_t[i]>0:
            temp[i]=1

def solveB(part,diff,num,questions):
    count = 0
    ques_per_topic = []
    question_paper =[]
    for topics in questions:
        tens = 0
        sixs = 0
        eights = 0
        fours = 0
        twelves = 0
        sixteens = 0
        for i in topics:
            if i[1]==part and i[2]==diff:
                if i[3]==10:
                    tens+=1
                elif i[3]==6:
                    sixs+=1
                elif i[3]==8:
                    eights+=1
                elif i[3]==4:
                    fours+=1
                elif i[3]==12:
                    twelves+=1
                elif i[3]==16:
                    sixteens+=1
        check = min(tens,sixs) + min(fours,twelves) + (eights//2) + sixteens
        ques_per_topic.append(check)

    if sum(ques_per_topic) < num:
        num = sum(ques_per_topic)
    
    temp=[0]*len(ques_per_topic)
    call2(temp,ques_per_topic)
            
    while(True):
        topic = random.choice(questions)
        question = random.choice(topic)

        if (question[1]==part) and (question[2]==diff) and temp[questions.index(topic)]==1:

            if question[3]==16:   
                #print("{}.) {} (16x1=16)".format(count+1,question[0]))
                question_paper.append(question)
                topic.remove(question)
                count += 1
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[3]==8:
                c = 0
                for i in questions:
                    for j in i:
                        if j[3] == 8 and j[1]==part and j[2]==diff:
                            c+=1
                if c > 1:
                    #print("{}.) {}(8x1=8)".format(count+1,question[0]))
                    question_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[3]==8) and (another[1]==part) and (another[2]==diff):
                            #print("{}.) {} (8x1=8)".format(count+1,another[0]))
                            question_paper.append(another)
                            topic.remove(another)
                            #print()
                            count+=1
                            break
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[3]==12:
                c = 0
                for i in questions:
                    for j in i:
                        if j[3] == 4 and j[1]==part and j[2]==diff:
                            c+=1
                if c > 0:
                    #print("{}.) {} (12x1=12)".format(count+1,question[0]))
                    question_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[3]==4) and (another[1]==part) and (another[2]==diff):
                            #print("{}.) {} (4x1=4)".format(count+1,another[0]))
                            question_paper.append(another)
                            topic.remove(another)
                            #print()
                            count+=1
                            break
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[3]==10:
                c = 0
                for i in questions:
                    for j in i:
                        if j[3] == 6 and j[1]==part and j[2]==diff:
                            c+=1
                if c > 0:
                    #print("{}.) {} (10x1=10)".format(count+1,question[0]))
                    question_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[3]==6) and (another[1]==part) and (another[2]==diff):
                            #print("{}.) {} (6x1=6)".format(count+1,another[0]))
                            question_paper.append(another)
                            topic.remove(another)
                            #print()
                            count+=1
                            break
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

        if count == num:
            if num==0:
                print("You didn't have questions to pick")
            break
        if temp.count(0)==len(temp):
            call2(temp,ques_per_topic)
