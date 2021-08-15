from django.views import View
from django.shortcuts import render
from ..models import Obon
from ..models import Result


class ResultsView(View):
    def get(self, request, *args, **kwargs):
        # 10人に満たなければ、名無しを生成
        while(len(Result.objects.all()) < 10):
            sample = Result.objects.create()
            sample.save()
        
        top_ten = Result.objects.order_by('result').reverse()[0:10]
        
        context = {
            'rank1': top_ten[0],
            'rank2': top_ten[1],
            'rank3': top_ten[2],
            'rank4': top_ten[3],
            'rank5': top_ten[4],
            'rank6': top_ten[5],
            'rank7': top_ten[6],
            'rank8': top_ten[7],
            'rank9': top_ten[8],
            'rank10': top_ten[9],
        }
        
        return render(request, 'results.html', context)