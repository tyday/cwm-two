from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def index(request):
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
            try:
                send_mail('chaneywealthmgmt: contact message', message, 'admin@chaneywealthmgmt.com', ['tyrday@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    
    return render(request,'cwm_index/index.html',{'form':form})