from django.shortcuts import render,HttpResponse,redirect
from app.models import *
from django.contrib import messages

def HOME(request):
    return render(request,'Student/home.html')


def VIEW_NOTIFICATIONS(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notifications = Student_Notification.objects.filter(student_id=student_id)
        context = {
            'notification':notifications,
        }
    return render(request,'Student/notifications.html',context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('View_notifications')

def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_Leave.objects.filter(student_id = student_id)

        context = {
            'student_leave_history':student_leave_history
        }
    return render(request,'Student/apply_leave.html',context)

def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student = Student.objects.get(admin=request.user.id)
        leave = Student_Leave(
            student_id=student,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'Leave successfully sent')
        return redirect('student_apply_leave')
    else:
        return HttpResponse("Invalid request method", status=400)


def STUDENT_VIEW_ATTENDANCE(request):
    student=Student.objects.get(admin=request.user.id)
    subjects=Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)
            # get_session_year = Session_Year.objects.get(id = session_year_id)
            attendance_report = Attendance_Report.objects.filter(attendance_id__subject_id = subject_id,student_id=student)
            # attendance = Attendance.objects.filter(subject_id = get_subject,attendance_data=attendance_date)
            
    context = {
    'subjects':subjects,
    'action':action,
    'get_subject':get_subject,
    'attendance_report':attendance_report,
    }
    return render(request, 'Student/view_attendance.html',context)

def VIEW_RESULT(request):
    mark = 0
    student = Student.objects.get(admin = request.user.id)
    result = StudentResult.objects.filter(student_id = student)
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark+exam_mark
    context = {
        'result':result,
        'mark':mark,
    }
    return render(request,'Student/view_result.html',context)