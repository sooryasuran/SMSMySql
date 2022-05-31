import datetime
from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from SchoolApp.forms import TeacherForm, LoginForm, StudentForm, TimeTableForm, CircularForm, FeedbackForm
from SchoolApp.models import Teacher, Login, Student, Attendance, TimeTable, Circular, Feedback


def homeview(request):
    return render(request, 'index.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_teacher:
                return redirect('teacherhome')
            elif user.is_student:
                return redirect('studenthome')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')


@login_required(login_url='loginview')
def teacherhome(request):
    return render(request, 'Teacher/teacherhome.html')


@login_required(login_url='loginview')
def adminhome(request):
    return render(request, 'ADMIN/adminhome.html')


@login_required(login_url='loginview')
def teacherregister(request):
    login_form = LoginForm()
    teacher_form = TeacherForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if login_form.is_valid() and teacher_form.is_valid():
            user = login_form.save(commit=False)
            user.is_teacher = True
            user.save()
            t = teacher_form.save(commit=False)
            t.user = user
            t.save()
            messages.info(request, 'Teacher registered successfully')
            return redirect('teacherview')
    return render(request, 'ADMIN/teacherregister.html', {'login_form': login_form, 'teacher_form': teacher_form})


@login_required(login_url='loginview')
def teacherview(request):
    teach = Teacher.objects.all()
    return render(request, 'ADMIN/teacherview.html', {'teach': teach})


@login_required(login_url='loginview')
def teacherupdate(request, id):
    teach = Teacher.objects.get(id=id)
    t = Login.objects.get(teacher=teach)
    if request.method == 'POST':
        form = TeacherForm(request.POST or None, instance=teach)
        login_form = LoginForm(request.POST or None, instance=t)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'Teacher updated successfully')
            return redirect('teacherview')
    else:
        form = TeacherForm(instance=teach)
        login_form = LoginForm(instance=t)
    return render(request, 'ADMIN/teacherupdate.html', {'form': form, 'login_form': login_form})


@login_required(login_url='loginview')
def teacherdelete(request, id):
    teach = Teacher.objects.get(id=id)
    t = Login.objects.get(teacher=teach)
    if request.method == 'POST':
        t.delete()
        messages.info(request, 'Teacher deleted successfully')
        return redirect('teacherview')
    else:
        return redirect('teacherview')


@login_required(login_url='loginview')
def logoutview(request):
    logout(request)
    return redirect('loginview')


@login_required(login_url='loginview')
def studenthome(request):
    return render(request, 'STUDENT/studenthome.html')


def studentregister(request):
    login_form = LoginForm()
    student_form = StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        student_form = StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            s = student_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Student registered successfully')
            return redirect('studentview')
    return render(request, 'Teacher/studentregister.html', {'login_form': login_form, 'student_form': student_form})


def studentview(request):
    stud = Student.objects.all()
    return render(request, 'Teacher/studentview.html', {'stud': stud})


@login_required(login_url='loginview')
def studentupdate(request, id):
    stud = Student.objects.get(id=id)
    s = Login.objects.get(student=stud)
    if request.method == 'POST':
        form = StudentForm(request.POST or None, instance=stud)
        login_form = LoginForm(request.POST or None, instance=s)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request, 'Student updated successfully')
            return redirect('studentview')
    else:
        form = StudentFor888m(instance=stud)
        login_form = LoginForm(instance=s)
    return render(request, 'Teacher/studentupdate.html', {'form': form, 'login_form': login_form})


@login_required(login_url='loginview')
def studentdelete(request, id):
    stud = Student.objects.get(id=id)
    s = Login.objects.get(student=stud)
    if request.method == 'POST':
        s.delete()
        messages.info(request, 'student deleted successfully')
        return redirect('studentview')
    else:
        return redirect('studentview')


def userprofile(request):
    u = request.user
    profile = Student.objects.filter(user_id=u)
    return render(request, 'STUDENT/studentprofile.html', {'profile': profile})


@login_required(login_url='loginview')
def student_teacher(request):
    prof = Teacher.objects.all()
    return render(request, 'STUDENT/student_teacher.html', {'prof': prof})


def TmtableView(request):
    Tm = TimeTable.objects.all()
    return render(request, 'ADMIN/Tmtableview.html', {'Tm': Tm})


def TmtableAdd(request):
    form = TimeTableForm()
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TmtableView')
    return render(request, 'ADMIN/TmtableAdd.html', {'form': form})


def TmtableDelete(request, id):
    if request.method == 'POST':
        form = TimeTable.objects.get(id=id)
        form.delete()
        return redirect('TmtableView')


def student_tmtable(request):
    st = TimeTable.objects.all()
    return render(request, 'STUDENT/student_tmtable.html', {'st': st})


def teacher_tmtable(request):
    tr = TimeTable.objects.all()
    return render(request, 'Teacher/student_tmtable.html', {'tr': tr})


def CircularView(request):
    cr = Circular.objects.all()
    return render(request, 'Teacher/CircularView.html', {'cr': cr})


def CircularAdd(request):
    form = CircularForm()
    if request.method == 'POST':
        form = CircularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CircularView')
    return render(request, 'Teacher/CircularAdd.html', {'form': form})


def CircularDelete(request, id):
    if request.method == 'POST':
        form = Circular.objects.get(id=id)
        form.delete()
        return redirect('CircularView')


def student_circular(request):
    st = Circular.objects.all()
    return render(request, 'STUDENT/student_circular.html', {'st': st})


def FeedbackView(request):
    fd = Feedback.objects.all()
    return render(request, 'Teacher/FeedbackView.html', {'fd': fd})


def FeedbackAdd(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('FeedbackView')
    return render(request, 'Teacher/FeedbackAdd.html', {'form': form})


def admin_feedback(request):
    ad = Feedback.objects.all()
    return render(request, 'ADMIN/AdminFeedbackView.html', {'ad': ad})


def feedbackreply(request, id):
    fd = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        fd.reply = r
        fd.save()
        messages.info(request, 'feedback reply updated')
        return redirect('admin_feedback')
    return render(request, 'ADMIN/feedbackreply.html', {'fd': fd})


def teacherfbreply(request):
    tr = Feedback.objects.all()
    return render(request, 'Teacher/teacherfbreply.html', {'tr': tr})


def add_attendance(request):
    student = Student.objects.all()
    return render(request, 'Teacher/student_list.html', {'student': student})


now = datetime.datetime.now()


@login_required(login_url='loginview')
def mark(request, id):
    user = Student.objects.get(id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's attendance already marked for this student")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request, "Attendance added successfully")
            return redirect('add_attendance')
        return render(request, 'Teacher/mark_attendance.html')


@login_required(login_url='loginview')
def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
        return render(request, 'Teacher/viewattendance.html', {'attendance': attendance})


def day_attendance(request,date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendance': attendance,
        'date': date
    }
    return render(request, 'Teacher/day_attendance.html', context)
def studentattendanceview(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'Student/studentattendanceview.html', {'attendance': attendance})

