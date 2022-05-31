from django.urls import path

from SchoolApp import views

urlpatterns = [
    path('',views.homeview,name='homeview'),
    path('loginview',views.loginview,name='loginview'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('teacherregister',views.teacherregister,name='teacherregister'),
    path('teacherview',views.teacherview,name='teacherview'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('teacherupdate/<int:id>',views.teacherupdate,name='teacherupdate'),
    path('teacherdelete/<int:id>',views.teacherdelete, name='teacherdelete'),
    path('logoutview', views.logoutview, name='logoutview'),
    path('studentview',views.studentview,name='studentview'),
    path('studentupdate/<int:id>',views.studentupdate,name='studentupdate'),
    path('studentdelete/<int:id>',views.studentdelete,name='studentdelete'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('student_teacher',views.student_teacher,name='student_teacher'),
    path('add_attendance',views.add_attendance,name='add_attendance'),
    path('mark/<int:id>',views.mark,name='mark'),
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('day_attendance/<date>',views.day_attendance,name='day_attendance'),
    path('TmtableView',views.TmtableView,name='TmtableView'),
    path('TmtableAdd',views.TmtableAdd,name='TmtableAdd'),
    path('TmtableDelete/<int:id>',views.TmtableDelete,name='TmtableDelete'),
    path('student_tmtable',views.student_tmtable,name='student_tmtable'),
    path('teacher_tmtable',views.teacher_tmtable,name='teacher_tmtable'),
    path('CircularView',views.CircularView,name='CircularView'),
    path('CircularAdd',views.CircularAdd,name='CircularAdd'),
    path('CircularDelete/<int:id>',views.CircularDelete,name='CircularDelete'),
    path('student_circular',views.student_circular,name='student_circular'),
    path('FeedbackView',views.FeedbackView,name='FeedbackView'),
    path('FeedbackAdd',views.FeedbackAdd,name='FeedbackAdd'),
    path('admin_feedback',views.admin_feedback,name = 'admin_feedback'),
    path('feedbackreply/<int:id>',views.feedbackreply,name='feedbackreply'),
    path('teacherfbreply',views.teacherfbreply,name='teacherfbreply'),
    path('studentattendanceview',views.studentattendanceview,name='studentattendanceview')

]