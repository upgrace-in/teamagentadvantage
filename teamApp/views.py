from django.shortcuts import render

# Create your views here.
def index(rst):
    return render(rst, 'index.html')