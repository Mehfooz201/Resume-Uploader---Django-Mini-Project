from django.shortcuts import render, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

# Create your views here.

class HomeView(View):  #Class Based Views
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'form': form, 'candidates':candidates})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'myapp/home.html', {'form': form})


class CandidateView(View):  #Class Based Views
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})
    


