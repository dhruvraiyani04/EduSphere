"""
URL configuration for SMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,hod_views,staff_views,student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout/', views.doLogout, name='dologout'),
    path('HOD/Home', hod_views.Home, name='hod_home'),
    path('Profile/', views.PROFILE, name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),
    path('Hod/Student/Add',hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>/',hod_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',hod_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>/',hod_views.DELETE_STUDENT,name='delete_student'),

    
    path('Hod/Staff/Add',hod_views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',hod_views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>/',hod_views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',hod_views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>/',hod_views.DELETE_STAFF,name='delete_staff'),


    path('Hod/Subject/Add',hod_views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',hod_views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:admin>/',hod_views.DELETE_SUBJECT,name='delete_subject'),


    path('Hod/Course/Add',hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',hod_views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',hod_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',hod_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',hod_views.DELETE_COURSE,name='delete_course'),


    path('Hod/Session/Add',hod_views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',hod_views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>',hod_views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',hod_views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',hod_views.DELETE_SESSION,name='delete_session'),


    path('Hod/Staff/Send_Staff_Notification',hod_views.SEND_STAFF_NOTIFICATION,name='send_staff_notification'),
    path('Hod/Staff/Save_Staff_Notification',hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('Hod/Staff/Leave_View',hod_views.LEAVE_VIEW,name='leave_view'),
    path('Hod/Staff/Approve_Leave/<str:id>',hod_views.APPROVE_LEAVE,name='approve_leave'),
    path('Hod/Staff/Disapprove_Leave/<str:id>',hod_views.DISAPPROVE_LEAVE,name='disapprove_leave'),

    path('Hod/Student/Leave_View',hod_views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('Hod/Student/Approve_Leave/<str:id>',hod_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('Hod/Student/Disapprove_Leave/<str:id>',hod_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),
    
    path('Hod/Student/Send_Student_Notification',hod_views.SEND_STUDENT_NOTIFICATION,name='send_student_notification'),
    path('Hod/Student/Save_Student_Notification',hod_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),
    path('Hod/View_Attendance',hod_views.VIEW_ATTENDANCE,name='view_attendance'),

    path('Staff/Home', staff_views.HOME, name='staff_home'),
    path('Staff/Notifications', staff_views.NOTIFICATIONS, name='notifications'),
    path('Staff/Markasdone/<str:status>', staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),
    path('Staff/Apply_Leave', staff_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_Leave_save/', staff_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),
    
    path('Staff/Take_Attendance', staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/Save_Attendance', staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/View_Attendance', staff_views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),
    path('Staff/Add/Result', staff_views.ADD_RESULT, name='add_result'),
    path('Staff/Save/Result', staff_views.STAFF_SAVE_RESULT, name='staff_save_result'),
    
    
    path('Student/Home', hod_views.Home, name='student_home'),
    path('Student/Notifications', student_views.VIEW_NOTIFICATIONS, name='View_notifications'),
    path('Student/Markasdone/<str:status>', student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_done'),
    path('Student/Apply_Leave', student_views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('Student/Apply_Leave_save/', student_views.STUDENT_APPLY_LEAVE_SAVE, name='student_apply_leave_save'),
    path('Student/View_Attendance', student_views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),
    path('Student/View_Result', student_views.VIEW_RESULT, name='view_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
