from django.shortcuts import render, redirect


def start(request):
    return render(request, 'reboot/index.html')

