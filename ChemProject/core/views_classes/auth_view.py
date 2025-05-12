from core.models import Chemist
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.hashers import check_password


class AuthView(View):
    def get(self, request):
        return render(request, 'auth.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        
        if [username, password] is not None:
            user = Chemist.objects.get(username=username, password=check_password(password))

        if Chemist.objects.filter(username=username, phone=phone).exists():
            user = Chemist.objects.get(username=username, phone=phone)
            login(request, user)
            return redirect('chat')

        user, created = Chemist.objects.get_or_create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        if created:
            user.set_password(password)
            user.save()

        login(request, user)
        return redirect('chat')