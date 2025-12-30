from django.shortcuts import render
from .models import Submission

def submit(request):
    return render(request, "onlinecourse/submit.html")

def show_exam_result(request):
    score = 100
    return render(request, "onlinecourse/result.html", {
        "score": score
    })

