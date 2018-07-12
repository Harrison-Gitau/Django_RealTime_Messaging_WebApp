from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm
# Create your views here.
def contact(request):
	title = 'contact'
	form = contactForm(request.POST or None)
	confirm_message = None


	if form.is_valid():
		name = form.cleaned_data['name']
		department = form.cleaned_data['department']
		comment = form.cleaned_data['comment']
		subject = 'Message from MYSITE.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
		title = "Thanks!"
		confirm_message = "Thanks for the message. We will get back right to you."
		form = None
		
	context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
	template = 'contact.html'
	return render(request,template,context)
