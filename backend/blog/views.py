#function based view.....
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')# can retrieve the submitted data
        return HttpResponse(f"Thanks, {name}!")
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')
'''#class based view....
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, Django World!")'''
'''	from django.shortcuts import redirect#for redirect to otherpage.'''
#class based post and get...
'''from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class Home(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        return HttpResponse(f"Hello, {name}!")'''