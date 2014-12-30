from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.forms import LegalSufficiencyForm
from app.models import LegalSufficiency
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

def home(request):
    query = LegalSufficiency.objects.all()
    in_draft = query.filter(status='draft')
    pending = query.filter(status='review')
    return render(request,'home.html', {'draft':in_draft, 'pending':pending})

###
# Create a new Document
###

@login_required
def new_legal_sufficiency(request):
    form = LegalSufficiencyForm()
    if request.method == "POST":
        form = LegalSufficiencyForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('home')
    return render(request,'app/new_legal_sufficiency.html', {'form':form})

class LegalSufficiencyUpdate(UpdateView):
    model = LegalSufficiency
    form_class = LegalSufficiencyForm

class LegalSufficiencyDelete(DeleteView):
    model = LegalSufficiency