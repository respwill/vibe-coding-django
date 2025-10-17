from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, '로그인 정보가 올바르지 않습니다.')
	else:
		form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('login')

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, '회원가입이 완료되었습니다. 로그인해 주세요.')
			return redirect('login')
		else:
			messages.error(request, '회원가입 정보가 올바르지 않습니다.')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})
