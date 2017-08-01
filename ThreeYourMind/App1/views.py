from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from App1.forms import ProfileImageForm
from App1.models import Profile
import requests
import webbrowser

class Test(TemplateView):
    template_name = 'Ok'


def parse(path):
    # path = 'block100.stl'
    myfile = open(path)
    showname = 'Johnsshipmodel'
    url = 'https://api.3yourmind.com/v1/uploads/'
    files = {'file': myfile}
    fields = {"origin": "python_test"}

    api_key = "9f5f00e6-d25b-482f-96b2-7860e9eaeea7"
    header = {"Authorization": "ApiKey " + api_key}

    # upload file
    response = requests.post(url, files=files, headers=header, data=fields).json()
    mydic = response
    webbrowser.open_new("https://api.3yourmind.com/v1/uploads/"+mydic['uuid'])
    print(mydic['uuid'])


def SaveProfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileImageForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.myfile = MyProfileForm.cleaned_data["myfile"]
            profile.save()
            saved = True
            parse(profile.myfile.path)

    else:
        MyProfileForm = ProfileImageForm()

    return render(request, 'saved.html', locals())
