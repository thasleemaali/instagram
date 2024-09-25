import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from insta.models import Login, Registration, Complaint, Post, Feedback, Report

def home(request):
    res=Post.objects.all()
    return render(request,'user/uhome.html',{'posts':res})

def ulogin(request):
    return render(request,'user/ulogin.html')

def ulogin_post(request):
    username = request.POST['loginame']
    password = request.POST['password']
    lobj = Login.objects.filter(username=username, password=password)
    if lobj.exists():
        lobj2 = Login.objects.get(username=username, password=password)
        request.session['lid'] = lobj2.id
        print(request.session['lid'])
        if lobj2.type == 'user':
            return HttpResponse('''<script>alert('Welcome to Home');window.location="/insta/home/"</script>''')
        elif lobj2.type == 'admin':
            return HttpResponse('''<script>alert('Welcome to Home');window.location="/insta/ahome/"</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location="/insta/ulogin/"</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location="/insta/ulogin/"</script>''')


def register(request):
    if request.method=='POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['passwordcon']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        bio = request.POST['bio']
        birthdate = request.POST['bdate']
        image=request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fn = fs.save(date,image)
        path = fs.url(date)

        lobj = Login()
        lobj.username = username
        lobj.password = password
        lobj.type = 'user'
        lobj.save()

        robj = Registration()
        robj.password = password
        robj.confirm_password = confirm_password
        robj.name = username
        robj.email = email
        robj.first_name = first_name
        robj.last_name = last_name
        robj.bio = bio
        robj.birthdate = birthdate
        robj.photo=path
        robj.LOGIN = lobj
        robj.save()
        return HttpResponse('''<script>('Registered Successfully');window.location="/insta/ulogin/"</script>''')
    else:
        return render(request,'user/usignup.html')

def register_post(request):
    password=request.POST['password']
    confirm_password=request.POST['passwordcon']
    name=request.POST['name']
    email=request.POST['email']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    bio = request.POST['bio']
    birthdate=request.POST['bdate']
    image = request.FILES['image']

    fs=FileSystemStorage()
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fn=fs.save(date,image)
    path=fs.url(date)

    lobj=Login()
    lobj.username=name
    lobj.password=password
    lobj.type='user'
    lobj.save()

    robj=Registration()
    robj.password=password
    robj.confirm_password=confirm_password
    robj.name=name
    robj.email=email
    robj.first_name = first_name
    robj.last_name = last_name
    robj.bio = bio
    robj.birthdate = birthdate
    robj.photo = path
    robj.LOGIN=lobj
    robj.save()
    return HttpResponse('''<script>('');window.location="/insta/ulogin/"</script>''')

def changepasw(request):
    return render(request,'user/uchangepassword.html')

def changepasw_post(request):
    current_password=request.POST['currentpassword']
    new_password=request.POST['newPassword']
    confim_password=request.POST['confirmPassword']
    pobj=Login.objects.filter(id=request.session['lid'],password=current_password)
    if pobj.exists():
        if new_password==confim_password:
            pobj1 = Login.objects.filter(id=request.session['lid'], password=current_password).update(password=new_password)
            return HttpResponse('''<script>alert('Succesfully updated');window.location="/insta/ulogin/"</script>''')
        else:
            return HttpResponse('''<script>alert('password didnot match');window.location="/insta/changepasw/"</script>''')
    else:
        return HttpResponse('''<script>alert('user not found');window.location="/insta/changepasw/"</script>''')

def view_registration(request):
    res=Registration.objects.get(LOGIN_id=request.session['lid'])
    res2=Post.objects.filter(REGISTRATION__LOGIN_id=request.session['lid'])
    return render(request,'user/uviewprofile.html',{'data':res,'data1':res2})

def edit(request):
    res=Registration.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/ueditprofile.html',{'editdata':res})

def edit_post(request):
    password = request.POST['password']
    confirm_password = request.POST['passwordcon']
    name = request.POST['name']
    email = request.POST['email']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    bio = request.POST['bio']
    birthdate = request.POST['bdate']

    if 'images' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d-%H%M%S")
        fn = fs.save(date,image)
        path = fs.url(date)

        robj = Registration.objects.get(LOGIN=request.session['lid'])
        robj.password = password
        robj.confirm_password = confirm_password
        robj.name = name
        robj.email = email
        robj.first_name = first_name
        robj.last_name = last_name
        robj.bio = bio
        robj.birthdate = birthdate
        robj.photo = path
        robj.save()

    lobj = Login.objects.get(id=request.session['lid'])
    lobj.username = name
    lobj.save()

    robj = Registration.objects.get(LOGIN=request.session['lid'])
    robj.password = password
    robj.confirm_password = confirm_password
    robj.name = name
    robj.email = email
    robj.first_name = first_name
    robj.last_name = last_name
    robj.bio = bio
    robj.birthdate = birthdate
    robj.photo = path
    robj.save()
    return HttpResponse('''<script>('Profile Edited');window.location="/insta/view_registration/"</script>''')

def send_complaint(request):
    return render(request,'user/send complaint.html')

def send_complaintpost(request):
    complaint=request.POST['comp']
    cobj=Complaint()
    cobj.complaint=complaint
    import datetime
    date=datetime.datetime.now().date()
    cobj.date=date
    cobj.reply='pending'
    cobj.status='pending'
    cobj.LOGIN_id=request.session['lid']
    cobj.save()
    return HttpResponse(''''<script>alert(' send successfully');window.location="/insta/home/"</script>''')

def view_reply(request):
    res=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/viewreply.html',{'data':res})

def post(request):
    res=Post.objects.all()
    return render(request,'user/addpost.html',{'posts':res})

def post_post(request):
    image = request.FILES['images']
    description=request.POST['description']

    fs = FileSystemStorage()
    import datetime
    date = datetime.datetime.now().date()
    fn = fs.save(date, image)
    path = fs.url(date)

    pobj=Post()
    pobj.description=description
    pobj.date=date
    pobj.REGISTRATION = Registration.objects.get(LOGIN=request.session['lid'])
    pobj.photo = path
    pobj.save()
    return HttpResponse('''<script>alert('Succesfully Added');window.location="/insta/home/"</script>''')

def view_post(request):
    res = Post.objects.get(LOGIN=request.session['lid'])
    return render(request, 'user/uhome.html', {'posts': res})

def usersearch(request):
    return render(request, 'user/usersearch.html')

def user_search_results(request):
    if request.method == 'POST':
        usearch = request.POST.get('usersearch')
        if usearch:
            res = Registration.objects.filter(name__contains=usearch)
            return render(request, 'user/view user.html', {"uview": res})
        else:
            return render('''<script>alert('User not found');window.location="/insta/usersearch/"</script>''')

def frequest(request):
    res=Registration.objects.all()
    return render(request,'user/sendrequest.html',{'data':res})


def usersend_feedback(request):
    return render(request,'user/sendfedback.html')

def usersend_feedback_post(request):
    feedback=request.POST['feed']

    fobj=Feedback()
    fobj.feedback=feedback
    import datetime
    date=datetime.datetime.now().date()
    fobj.send_date=date
    fobj.status='pending'
    fobj.REGISTRATION = Registration.objects.get(LOGIN_id=request.session['lid'])
    fobj.save()
    return HttpResponse(''''<script>alert('Your Feedback has Sended');window.location="/insta/home/"</script>''')

def reportuser(request,id):
    return render(request,'user/ureport.html',{"id":id})

def reportuser_post(request):
    report = request.POST['report']
    id = request.POST['id']
    robj = Report()
    robj.report = report

    import datetime
    date = datetime.datetime.now().date()
    robj.send_date = date
    robj.reply = 'pending'
    robj.status = 'pending'
    robj.REGISTRATION = Registration.objects.get(LOGIN_id=request.session['lid'])
    robj.against_user=Registration.objects.get(id=id)
    robj.save()
    return HttpResponse(''''<script>alert('reported successfully');window.location="/insta/home/"</script>''')

#################################################################################################################################

def adminhome(request):
    return render(request,'admin/adhome.html')

def adminusers(request):
    res = Registration.objects.all()
    return render(request,'admin/users.html',{"user":res})

def adminusersearch(request):
    search=request.POST['search']
    res=Registration.objects.filter(name__contains=search)
    return render(request,'admin/users.html',{"user":res})

def adminreply(request,id):
    return render(request,'admin/sendreply.html',{"id":id})

def adminreply_post(request):
    reply=request.POST['reply']
    id=request.POST['id']
    cobj=Complaint.objects.get(id=id)
    cobj.reply=reply
    cobj.status="replied"
    cobj.save()
    return HttpResponse(''''<script>alert('replied succcessfully');window.location="/insta/adminview_complaint/"</script>''')

def adminview_complaint(request):
    res=Complaint.objects.all
    return render(request,'admin/complaint.html',{"com":res})

def compsearch_post(request):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=Complaint.objects.filter(date__range=[fdate,tdate])
    return render(request,'Admin/adviewcomplaint.html',{"com":res})

def adminview_feedback(request):
    res=Feedback.objects.all
    return render(request,'admin/feedback.html',{"cview":res})

def admindatesearch_post(request):
    sdate=request.POST['sdate']
    ddate=request.POST['ddate']
    res=Feedback.objects.filter(send_date__range=[sdate,ddate])
    return render(request, 'Admin/adminviewfeedback.html',{"cview":res})
