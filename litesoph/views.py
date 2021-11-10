from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,"litesoph/index.html")

def about(request):
   return render(request, "litesoph/about.html") 

def features(request):
   return render(request, "litesoph/features.html")

def download(request):
    return render(request, "litesoph/download.html")

def resources(request):
    return render(request, "litesoph/resources.html")    

def github(request):
    return render(request, "litesoph/github.html")

def gui(request):
    return render(request, "litesoph/gui.html")  

def contact(request):
    return render(request, "litesoph/contact.html")

def news(request):
    return render(request, "litesoph/news.html") 

def faq(request):
    return render(request, "litesoph/faq.html")

def people(request):
    return render(request, "litesoph/people.html")

def manual(request):
    return render(request, "litesoph/manual.html")

def tutorials(request):
    return render(request, "litesoph/tutorials.html")    

def tools(request):
    return render(request, "litesoph/tools.html") 

def visualization(request):
    return render(request, "litesoph/visualization.html")

def publications(request):
    return render(request, "litesoph/publications.html")    