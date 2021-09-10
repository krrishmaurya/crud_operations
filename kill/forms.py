from django import forms
 
class Student(forms.Form):
    student_name = forms.CharField(max_length=30)
    roll_no = forms.IntegerField()
