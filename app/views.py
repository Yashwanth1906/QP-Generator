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
        temp.append(i['difficulty'])
        temp.append(i['marks'])
        temp.append(i['topic'])
        questions1.append(temp)
    topics = []
    for i in questions1:
        if i[3] not in topics:
            topics.append(i[3])
    print(topics)
    x = []
    for i in range(len(topics)):
        temp = []
        x.append(temp)
    print(x)
    for k,j in enumerate(topics):
        for i in questions1:
            if j == i[3]:
                x[k].append(i)
    global questionb_paper
    global questiona_paper
    global message
    y = message
    solveA(1,parta_diff1,x)
    for i in questiona_paper:
        for j in x:
            if i in j:
                print("AYES")
    solveA(2,parta_diff2,x)
    for i in questiona_paper:
        for j in x:
            if i in j:
                print("AYES")
    solveA(3,parta_diff3,x)
    for i in questiona_paper:
        for j in x:
            if i in j:
                print("AYES")
    solveB(1,partb_diff1,x)
    for i in questionb_paper:
        for j in x:
            if i in j:
                print("BYES")
    solveB(2,partb_diff2,x)
    for i in questionb_paper:
        for j in x:
            if i in j:
                print("BYES")
    solveB(3,partb_diff3,x)
    for i in questionb_paper:
        for j in x:
            if i in j:
                print("BYES")
    print(questionb_paper)
    z = questionb_paper
    partaqns= []
    for i in questiona_paper:
        partaqns.append(i[0])
    questionb_paper = []
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
    questioninner = []
    for i in z:
        questioninner.append(i)
    for i in questioninner:
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
    print("a11:",end="")
    print(a11)
    print("b11:",end="")
    print(b11)
    message = ""
    counta = 1
    return render(r,"show.html",{'parta':partaqns,'partb':z,'a':code,'b':set,'c':branch,'d':date,'e':year,'f':semester,'g':assessment,'11a':a11,'11b':b11,'12a':a12,'12b':b12,'13a':a13,'13b':b13,'14a':a14,'14b':b14,'15a':a15,'15b':a15})
    
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

import random
def call(topics,li,diff,questions):
    for i in range(topics):
        for j in questions[i]:
            if (j[2]==2) and (j[1]==diff):
                li[i]=1
                break
questiona_paper = []
questionb_paper = []
def solveA(diff,num,questions):
    global questiona_paper
    check = 0
    topics = 0
    for i in questions:
        topics+=1                         
        for j in i:                       
            if j[2]==2 and j[1]==diff: 
                check+=1
    if check < num:
        num = check

    li = [0]*topics
    call(topics,li,diff,questions)
    count = 0
    while(True):
        if (num==0):
            break
        topic = random.choice(questions)
        question = random.choice(topic)
        if (question[2]==2) and (question[1]==diff) and li[questions.index(topic)]==1:
            #print("{}.) {} (2x1=2)".format(count+1,question[0]))
            questiona_paper.append(question)
            topic.remove(question)
            count += 1
            li[questions.index(topic)]=0
            if count == num:
                break
            if li.count(0)==len(li):
                #li=[0]*topics
                call(topics,li,diff,questions)

def call2(temp,q_p_t):
    for i in range(len(q_p_t)):
        if q_p_t[i]>0:
            temp[i]=1

def solveB(diff,num,questions):
    count = 0
    ques_per_topic = []
    for topics in questions:
        tens = 0
        sixs = 0
        eights = 0
        fours = 0
        twelves = 0
        sixteens = 0
        for i in topics:
            if (i[2] in [4,6,10,12,16]) and i[1]==diff:
                if i[2]==10:
                    tens+=1
                elif i[2]==6:
                    sixs+=1
                elif i[2]==8:
                    eights+=1
                elif i[2]==4:
                    fours+=1
                elif i[2]==12:
                    twelves+=1
                elif i[2]==16:
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

        if (question[2] in [4,6,10,12,16]) and (question[1]==diff) and temp[questions.index(topic)]==1:

            if question[2]==16: 
                #print("{}.) {} (16x1=16)".format(count+1,question[0]))
                questionb_paper.append(question)
                topic.remove(question)
                count += 1
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[2]==8:
                c = 0
                for i in questions:
                    for j in i:
                        if j[2] == 8 and j[1]==diff:
                            c+=1
                if c > 1:
                    #print("{}.) {}(8x1=8)".format(count+1,question[0]))
                    questionb_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[2]==8) and (another[1]==diff):
                            #print("{}.) {} (8x1=8)".format(count+1,another[0]))
                            questionb_paper.append(another)
                            topic.remove(another)
                            #print()
                            count+=1
                            break
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[2]==12:
                c = 0
                for i in questions:
                    for j in i:
                        if j[2] == 4 and j[1]==diff:
                            c+=1
                if c > 0:
                    #print("{}.) {} (12x1=12)".format(count+1,question[0]))
                    questionb_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[2]==4) and (another[1]==diff):
                            #print("{}.) {} (4x1=4)".format(count+1,another[0]))
                            questionb_paper.append(another)
                            topic.remove(another)
                            #print()
                            count+=1
                            break
                temp[questions.index(topic)]=0
                ques_per_topic[questions.index(topic)]-=1

            elif question[2]==10:
                c = 0
                for i in questions:
                    for j in i:
                        if j[2] == 6 and j[1]==diff:
                            c+=1
                if c > 0:
                    #print("{}.) {} (10x1=10)".format(count+1,question[0]))
                    questionb_paper.append(question)
                    topic.remove(question)
                    while True:
                        another = random.choice(topic)
                        if (another[2]==6) and (another[1]==diff):
                            #print("{}.) {} (6x1=6)".format(count+1,another[0]))
                            questionb_paper.append(another)
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
