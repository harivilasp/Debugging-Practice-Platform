from django.shortcuts import render
import requests
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def index(request):
    
    print(os.getcwd())
    ques=open("assets/ques.txt","r")
    questext=ques.readlines()
    ques.close()
    ans=open("assets/ans.txt","r")
    anstext=ans.readlines()
    ans.close()
    k = {'ques': questext, 'c' : anstext }
    return render(request, 'allutility/index.html', k)



def home(request):
    return render(request, 'allutility/home.html')

def ide(request):
    if request.method == 'POST':

        cod = request.POST['co']
        inp = request.POST['input']
        lang = request.POST['lang']

        print(lang)

        url = "https://ide.geeksforgeeks.org/main.php"

        data = {
            'lang': lang,
            'code': cod,
            'input': inp,
            'save': True
        }

        r = requests.post(url, data=data)
        
        #k = {'s': r.json(), 'c': cod, 'i':inp}
        sid=r.json()['sid']
        url = "https://ide.geeksforgeeks.org/submissionResult.php"
        
        data = {
            'sid': sid,
            'requestType': 'fetchResults',
        }
        r = requests.post(url, data=data)
        while(r.json()['status']=='IN-QUEUE'):
            time.sleep(0.1)
            r = requests.post(url, data=data)
        r = requests.post(url, data=data)
        print(r.json())
        outp = ""
        try:
            outp=r.json()['output']
        except:
            outp=r.json()['rntError']
        k = {'s': outp, 'c': cod, 'i':inp}

        return render(request, 'allutility/index.html', k)



