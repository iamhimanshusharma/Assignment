from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Question, Grade, Subject

# Create your views here.
def home(request):
    return render(request, 'index.html')

def insert(request):
    if request.method == 'POST':
        file = request.FILES['file'].read().decode('utf-8')          

        datas = file.split("\n")

        for i in range(1, len(datas)):
            rows_data = datas[i].split(",")
            if (len(rows_data) == 5):
                grade_data = Grade.objects.get(GradeID=rows_data[2])
                subject_data = Subject.objects.get(SubjectID=rows_data[3])
                upload = Question(QuestionsText=rows_data[1], GradeId=rows_data[2], Grade=grade_data.Grade, SubjectID=rows_data[3], Subject=subject_data.Subject)
                upload.save()
            else:
                continue
    return render(request, 'success.html')

def showdata(request):
    alldata = Question.objects.all().order_by('id')
    params = {'alldata':alldata}
    return render(request, 'showdata.html', params)

def update(request):
    if request.method == 'POST':
        question_id = request.POST.get('questionid')

        get_data = Question.objects.get(pk=question_id)

        params = {'get_data':get_data}

        return render(request, 'update.html', params)

def updated(request):
    if request.method == 'POST':
        question_id = request.POST.get('id')
        question_text = request.POST.get('questiontext')
        gradeid = request.POST.get('gradeid')
        subjectid = request.POST.get('subjectid')

        data = Question.objects.get(pk=question_id)
        data.QuestionsText = question_text
        data.GradeId = gradeid
        grade = Grade.objects.get(GradeID=gradeid)
        data.Grade = grade.Grade
        data.SubjectID = subjectid
        subject = Subject.objects.get(SubjectID=subjectid)
        data.Subject = subject.Subject
        data.Grade = grade.Grade
        data.save()

        return render(request, 'success.html')