from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def userLogin(request):
	data={}
	if request.user.is_authenticated():
		redirect('/hisab/expenses')
	if request.method=='GET':
		data={'form':LoginForm()}
		return render(request,'hisab/index.html',data)
	elif request.method=='POST':
		loginForm=LoginForm(request.POST)
		result=False
		msg=''
		if loginForm.is_valid():
			email=loginForm.cleaned_data['email']
			password=loginForm.cleaned_data['password']
			user=authenticate(email=email, password=password)
			if user:
				login(request,user)
				return render(request,'hisab/list_expense.html',data);
			else:
				msg='Invalid email and password combination.'
				return render(request,'hisab/index.html',data);
		else:
			data['form']=loginForm
			return render(request,'hisab/index.html',data);

def userLogout(request):
	logout(request)
	data={'form':LoginForm()}
	return redirect('/hisab/login/')

@login_required
def listExpenses(request):
	data={}
	return render(request,'hisab/list_expense.html',data)