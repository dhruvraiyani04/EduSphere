from django.shortcuts import render, HttpResponse, redirect
from app.models import *
from django.contrib import messages


def HOME(request):
    return render(request, "Staff/home.html")


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        notifications = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {
            "notification": notifications,
        }
    return render(request, "Staff/notifications.html", context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    print(notification.status)
    notification.save()
    return redirect("notifications")


def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

        context = {"staff_leave_history": staff_leave_history}
    return render(request, "Staff/apply_leave.html", context)


def STAFF_APPLY_LEAVE_SAVE(request):
    print(f"Request method: {request.method}")  # Debugging statement
    if request.method == "POST":
        leave_date = request.POST.get("leave_date")
        leave_message = request.POST.get("leave_message")

        staff = Staff.objects.get(admin=request.user.id)
        leave = Staff_Leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, "Leave successfully sent")
        return redirect("staff_apply_leave")
    else:
        return HttpResponse("Invalid request method", status=400)


def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")

    get_subject = None
    get_session_year = None
    students = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            session_year_id = request.POST.get("session_year_id")

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
    context = {
        "subject": subject,
        "session_year": session_year,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "action": action,
        "students": students,
    }
    return render(request, "Staff/take_attendance.html", context)


# def STAFF_SAVE_ATTENDANCE(request):
#     if request.method == "POST":
#         subject_id = request.POST.get('subject_id')
#         session_year_id = request.POST.get('session_year_id')
#         attendance_date = request.POST.get('attendance_date')
#         student_id = request.POST.get('student_id')


#         get_subject = Subject.objects.get(id = subject_id)
#         get_session_year = Session_Year.objects.get(id = session_year_id)

#         attendance = Attendance(
#             subject_id = get_subject,
#             attendance_data = attendance_date,
#             session_year_id = get_session_year,
#         )
#         attendance.save()
#         for i in student_id:
#             stud_id = i
#             int_stud = int(stud_id)
#             print(stud_id)
#             p_students = Student.objects.get(id=int_stud)
#             attendance_report = Attendance_Report(
#                 student_id = p_students,
#                 attendance_id = attendance,
#             )
#             attendance_report.save()
#     return redirect('staff_take_attendance')


def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        session_year_id = request.POST.get("session_year_id")
        attendance_date = request.POST.get("attendance_date")
        student_ids = request.POST.getlist(
            "student_id[]"
        )  # Fetching multiple student IDs as a list

        # Fetch the subject and session year objects
        try:
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
        except Subject.DoesNotExist:
            return HttpResponse("Subject does not exist")
        except Session_Year.DoesNotExist:
            return HttpResponse("Session year does not exist")

        # Create attendance entry
        attendance = Attendance(
            subject_id=get_subject,
            attendance_data=attendance_date,
            session_year_id=get_session_year,
        )
        attendance.save()

        # Loop through the student IDs and save attendance for each
        for stud_id in student_ids:
            try:
                int_stud = int(stud_id)
                p_student = Student.objects.get(id=int_stud)

                # Create and save attendance report
                attendance_report = Attendance_Report(
                    student_id=p_student,
                    attendance_id=attendance,
                )
                attendance_report.save()

            except Student.DoesNotExist:
                # Handle missing student
                print(f"Student with ID {int_stud} does not exist")
                return HttpResponse(f"Student with ID {int_stud} does not exist")

        return redirect("staff_take_attendance")

    return redirect("staff_take_attendance")


def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            session_year_id = request.POST.get("session_year_id")
            attendance_date = request.POST.get("attendance_date")
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            attendance = Attendance.objects.filter(
                subject_id=get_subject, attendance_data=attendance_date
            )
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(
                    attendance_id=attendance_id
                )

    context = {
        "subject": subject,
        "session_year": session_year,
        "action": action,
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "attendance_date": attendance_date,
        "attendance_report": attendance_report,
    }
    return render(request, "Staff/view_attendance.html", context)


def ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)

    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get("action")
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            session_year_id = request.POST.get("session_year_id")

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)

    context = {
        "subjects": subjects,
        "session_year": session_year,
        "action": action,
        "get_subject": get_subject,
        "get_session": get_session,
        "students": students,
    }

    return render(request, "Staff/add_result.html", context)


def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        session_year_id = request.POST.get("session_year_id")
        student_id = request.POST.get("student_id")
        assignment_mark = request.POST.get("assignment_mark")
        Exam_mark = request.POST.get("Exam_mark")

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(
            subject_id=get_subject, student_id=get_student
        ).exists()
        if check_exist:
            result = StudentResult.objects.get(
                subject_id=get_subject, student_id=get_student
            )
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect("add_result")
        else:
            result = StudentResult(
                student_id=get_student,
                subject_id=get_subject,
                exam_mark=Exam_mark,
                assignment_mark=assignment_mark,
            )
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect("add_result")
