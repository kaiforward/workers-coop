from django.shortcuts import render
from .models import HomeText, AboutText, MembersAgreement
# Create your views here.
def home(request):
	home = HomeText.objects.all()
	return render(request, 'home.html', {'home': home})

# Create your views here.
def about(request):
	about = AboutText.objects.all()
	return render(request, 'about.html', {'about': about})

# Create your views here.
def members_agreement(request):
	members_agreement = MembersAgreement.objects.all()
	return render(request, 'members_agreement.html', {'members_agreement': members_agreement})