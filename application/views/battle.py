from django.views import View
from django.shortcuts import render
from ..models import Obon
from ..models import Result

class BattleView(View):
    def get(self, request, *args, **kwargs):
        # 飛距離を計算
        
        
        obon = Obon.objects.get(user_id=request.user.id)
        context = {
            'obon' : obon
        }
        
        return render(request, 'battle.html', context)