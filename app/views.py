from django.shortcuts import render
from app.forms import LegalSufficiencyForm
# Create your views here.

###
# Create a new Document
###
def new_legal_sufficiency(request):
    if request.method == "POST":
        form = LegalSufficiencyForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('/')
    form = LegalSufficiencyForm()
    return render(request,'new_legal_sufficiency.html', {'form':form})
