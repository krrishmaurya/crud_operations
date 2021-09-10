
from django.shortcuts import redirect, render
from django.views import View
from . import forms
from . import models









class Home(View):
    
    def get(self,request):
        content={
            'student_details':models.Student.objects.all(),
             'Student_form':forms.Student()

        }
        return render(request,'Index.html',content)


    def post(self,request):
        student_name=request.POST['student_name']
        roll_no = request.POST['roll_no']
        new_data=models.Student(student_name=student_name,roll_no=roll_no) 
        new_data.save()   
        return redirect('/')


class Delete_task(Home):
    def post(self, request):
        student_id=request.POST['student_id']
        detail=models.Student.objects.filter(id=student_id)
        detail.delete()
        return redirect('/')
     

