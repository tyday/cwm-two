from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
        # return HttpResponse('<h1>Page not found</h1>')
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_name = form.cleaned_data['from_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            # message = f"Name: {from_name} \r\nSender: {from_email} \nSubject:{subject} \n{message}"
            message = f"""Name: {from_name}
                        Sender: {from_email}
                        Subject:{subject}
                        {message}"""
            # message = "this is a message\r\nnewline \r\n other new line"
            print(message)
            subject = 'chaneywealthmgmt: contact message'
            from_email = 'admin@tylerday.net'
            to_email = ['tyrday@gmail.com','tyrday@live.com','tyrolia@habernashing.com']
            try:
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    
    return render(request,'cwm_index/index.html',{'form':form})