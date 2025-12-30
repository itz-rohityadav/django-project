from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Question, Choice, Submission

@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    if request.method == "POST":
        submission = Submission.objects.create(user=request.user)

        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                submission.choices.add(choice)

        submission.save()
        return render(request, "onlinecourse/result.html", {
            "course": course,
            "submission": submission
        })

    return render(request, "onlinecourse/submit.html", {
        "course": course,
        "questions": questions
    })


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    total_questions = submission.choices.count()
    correct_answers = submission.choices.filter(is_correct=True).count()

    score = 0
    if total_questions > 0:
        score = int((correct_answers / total_questions) * 100)

    return render(request, "onlinecourse/result.html", {
        "course": course,
        "score": score,
        "correct_answers": correct_answers,
        "total_questions": total_questions
    })
