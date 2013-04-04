from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
import re

from blog.models import *

USER_RE = re.compile(r"^[a-zA-Z0-9]{3,20}$")
def valid_username(username):
	return USER_RE.match(username)
		
PASS_RE = re.compile("^.{3,20}$")
def valid_password(password):
	return USER_RE.match(password)  
		
EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")   
def valid_email(email):
	return EMAIL_RE.match(email)

def create_user(request):

	if request.method == 'GET': 
		return render_to_response('create_user.html', 
				RequestContext(request))

	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = request.POST['password']
		confirm = request.POST['confirm']
		email = request.POST['email']
		empty_field_error = invalid_username_error = invalid_password_error = \
			invalid_email_error = different_passwords_error = ""

		if not all([username, first_name, last_name, password, email]):
			empty_field_error = "All fields must be completed."
			return render_to_response('create_user.html',
				{
				'empty_field_error': empty_field_error,
				'username': username,
				'first_name': first_name,
				'last_name': last_name,
				'email': email
				}, 
				context_instance=RequestContext(request))

		if not valid_username(username):
			invalid_username_error = "Username must be between 3-20 alphanumeric characters"
		
		if not valid_password(password):
			invalid_password_error = "Password must be between 3-20 characters."
		
		if not valid_email(email):
			invalid_email_error = "That does not appear to be a valid_email."
	   
		if password != confirm:
			different_passwords_error = "Your passwords do not match."
		
		if User.objects.filter (username=username):
			invalid_username_error = "That username already exists."
	   
		if any([invalid_username_error, invalid_password_error,
						invalid_email_error, different_passwords_error]):
			return render_to_response('create_user.html',
				{
				'invalid_username_error': invalid_username_error,
				'invalid_password_error': invalid_password_error,
				'invalid_email_error': invalid_email_error,
				'different_passwords_error': different_passwords_error,
				'username': username,
				'first_name': first_name,
				'last_name': last_name,
				'email': email
				}, 
				context_instance=RequestContext(request))
		
		else:
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			request.session['user'] = user
			return redirect('/' + str(user.username) + '/')

def main(request, username=None):
	#front page of blog
	users = User.objects.all()[:5]
	if username:
		try:
			author = User.objects.get(username__iexact = username)
		except User.DoesNotExist:
			error_message = "Sorry, there is no author with that name."
			return render_to_response("error_page.html", 
									   dict(error_message = error_message))
		posts = Post.objects.filter(author = author).order_by("-created")
	
	else:
		posts = Post.objects.all()
		author = None

	paginator = Paginator(posts, 2)

	try: 
		page = int(request.GET.get("page", '1'))
	except ValueError:
		page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("list.html", dict(posts = posts, 
												user = request.user, 
												author = author,
												users = users))

def post(request, post_key):
	post = Post.objects.get(id = post_key)
	return render_to_response("full_entry.html", dict(post=post))

def logout(request):
	#logsout user and returns to main page
	logout(request)
	return redirect('/')


