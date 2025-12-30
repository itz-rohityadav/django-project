from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path(
        'course_id/<int:course_id>/submit/',
        views.submit,
        name='submit'
    ),
    path(
        'course_id/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]
