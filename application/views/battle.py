from django.views import View
from django.shortcuts import render
from ..models import Obon
from ..models import Result
from django.contrib.auth import get_user_model
import json
import math

User = get_user_model()

class BattleView(View):
    def get(self, request, *args, **kwargs):
        obon = Obon.objects.get(user_id=request.user.id)

        # 時間を計算
        time =  math.floor((obon.size + obon.wise + obon.weight + obon.motivation) / 12)

        # 飛距離を計算
        distance = time * 90 
        result = Result.objects.create(name=obon.name, result=distance)
        result.save()
        
        data = {
            "imageUrl" : obon.image.url,
            "time" : time,
        }
        
        return render(request, 'battle.html', {'data_json': json.dumps(data)})