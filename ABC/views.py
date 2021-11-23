from django.shortcuts import render
import csv
from .models import Contact

# Create your views here.

def index(request):
    return render(request,"ABC/index.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"ABC/contact.html")

def NIT(request):
    return render(request,"ABC/NIT.html")

def IIT(request):
    return render(request,"ABC/IIT.html")

def IIIT(request):
    return render(request,"ABC/IIIT.html")


def IIIT2(request):
    if request.method=="POST":
        print("hello")
        name=request.POST.get('name','')
        rank=request.POST.get('rank','')
        branch=request.POST.get('branch','')
        cast=request.POST.get('cast','')
        gender=request.POST.get('gender','')
        rank=int(rank)
        # main program
        
    
    with open('D:\StuDyMateRiAl\Engineering_Web\CollageDost\ABC\IIIT.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        j=0
        final=[]
        catogery={}
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(row[3]==cast):
                    line_count += 1
                    try:
                        if( int(row[6])>=rank):
                            if(branch==row[1]):
                                catogery["institute"]=row[0]
                                catogery["opening"]=row[5]
                                catogery["closing"]=row[6]
                                final.append(catogery)
                                catogery={}

                    except:
                        pass
                elif(line_count==586):
                        break
                else:
                    line_count += 1
                    continue
        print(f'Processed {line_count} lines.')
    return render(request,"ABC/IIIT.html",{"final":final,"name":name})

def NIT2(request):
    if request.method=="POST":
        print("hello")
        name=request.POST.get('name','')
        rank=request.POST.get('rank','')
        branch=request.POST.get('branch','')
        cast=request.POST.get('cast','')
        gender=request.POST.get('gender','')
        Quota=request.POST.get('Quota','')
        rank=int(rank)
        # main program
        
    with open(r"D:\StuDyMateRiAl\Engineering_Web\CollageDost\ABC\NIT.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        j=0
        final=[]
        catogery={}
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(row[3]==cast):
                    line_count += 1
                    try:
                        if( int(row[6])>=rank):
                            if(branch==row[1]):
                                catogery["institute"]=row[0]
                                catogery["opening"]=row[5]
                                catogery["closing"]=row[6]
                                final.append(catogery)
                                catogery={}

                    except:
                        pass
                elif(line_count==5659):
                        break
                else:
                    line_count += 1
                    continue
        print(f'Processed {line_count} lines.')
    return render(request,"ABC/IIT.html",{"final":final,"name":name})

def IIT2(request):
    if request.method=="POST":
        print("hello")
        name=request.POST.get('name','')
        rank=request.POST.get('rank','')
        branch=request.POST.get('branch','')
        cast=request.POST.get('cast','')
        gender=request.POST.get('gender','')
        rank=int(rank)
        # main program
        
    
    with open('D:\StuDyMateRiAl\Engineering_Web\CollageDost\ABC\josaa.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        j=0
        final=[]
        catogery={}
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(row[3]==cast):
                    line_count += 1
                    try:
                        if( int(row[6])>=rank):
                            if(branch==row[1]):
                                catogery["institute"]=row[0]
                                catogery["opening"]=row[5]
                                catogery["closing"]=row[6]
                                final.append(catogery)
                                catogery={}

                    except:
                        pass
                elif(line_count==2718):
                        break
                else:
                    line_count += 1
                    continue
        print(f'Processed {line_count} lines.')
    return render(request,"ABC/IIT.html",{"final":final,"name":name})


def JEE(request):
    return render(request,"ABC/JEE.html")

def JEE2(request):
    if request.method=="POST":
        print("hello")
        name=request.POST.get('name','')
        rank=request.POST.get('rank','')
        branch=request.POST.get('branch','')
        

        # main program
        
    
    with open('D:\StuDyMateRiAl\Engineering_Web\CollageDost\ABC\JEE.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        j=0
        final=[]
        catogery={}
        
        for row in csv_reader:
            print(row[1])
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if(branch==row[5]):
                    try:
                        rank2=""
                        for ele in str(row[1]):
                            if(ele!=" "):
                                rank2+=ele
                            else:
                                break
                        if(rank2>=rank):
                            catogery["institute"]=row[3]
                            catogery["rank"]=row[1]
                            catogery["choice"]=row[2]
                            final.append(catogery)
                            catogery={}
                    except:
                        pass
                elif(line_count==1992):
                        break
                else:
                    line_count += 1
                    continue
        print(f'Processed {line_count} lines.')
    return render(request,"ABC/JEE.html",{"final":final,"name":name})
    