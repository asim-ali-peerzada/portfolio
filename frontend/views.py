from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Process form data (e.g., send email)
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],  # Replace with your email address or list
            fail_silently=False,
        )


    return render(request, 'index.html')
    



# views.py




