from django.views import View
from django.shortcuts import render
from ..models import Obon
from ..models import Result
from django.contrib.auth import get_user_model

User = get_user_model()

class BattleView(View):
    def get(self, request, *args, **kwargs):
        obon = Obon.objects.get(user_id=request.user.id)
        
        # 飛距離を計算
        distance = obon.size + obon.wise + obon.weight + obon.motivation
        result = Result.objects.create(name=obon.name, result=distance)
        result.save()
        
        context = {
            'obon' : obon
        }
        
        return render(request, 'battle.html', context)