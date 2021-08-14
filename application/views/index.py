from django.views import View
from django.shortcuts import render,redirect
from ..models import Obon
import json

item_moneys = {'takoyaki':100, 'ringoame': 150}

class IndexView(View):
    def get(self, request, *args, **kwargs):
        if(Obon.objects.filter(user_id=request.user.id).exists()):
            obon = Obon.objects.get(user_id=request.user.id)
        else:
            return redirect('create')
        
        context = {
            'obon' : obon
        }
        
        return render(request, 'registration/index.html', context)
    
    
    # foodstore からのrender時に呼ばれる
    def post(self, request, *args, **kwargs):
        obon = Obon.objects.get(user_id=request.user.id)
        context = {
            'obon' : obon
        }
        
        return render(request, 'registration/index.html', context)