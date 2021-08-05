from django.shortcuts import render,redirect
import pickle
import os
from . models import Prediction

# Create your views here.

def index(request):
    res=Prediction.objects.all()
    return render(request,"index.html",{'res':res})
def test(request):
    ppw=int(request.POST['ppw'])
    pn=int(request.POST['pn'])
    mi=int(request.POST['mi'])
    appw=int(request.POST['appw'])
    modulepath=os.path.dirname(__file__)
    model=pickle.load(open(os.path.join(modulepath,'taxi.pkl'),'rb'))
    res=str(model.predict([[ppw,pn,mi,appw]])[0].round(4))
    pre=Prediction(ppw=str(ppw),pn=str(pn),mi=str(mi),appm=str(appw),result=res)  #ORM (Object relationship mapping)
    pre.save()
    return redirect('index')









