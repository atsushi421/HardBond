from django.views import View
from django.shortcuts import render, redirect
from ..models import Obon
import json

item_moneys = {'takoyaki':100, 'ringoame': 150, 'yakisoba':200, 'tyokobanana':230}
takoyaki = {'size': 3, 'wise': 1, 'weight': 4, 'motivation': 2}
ringoame = {'size': 2, 'wise': 0, 'weight': 1, 'motivation': 2}
yakisoba = {'size': 1, 'wise': 5, 'weight': 2, 'motivation': 6}
tyokobanana = {'size': 0, 'wise': 0, 'weight': 0, 'motivation': 10}


class FoodStoreView(View):
    def get(self, request, *args, **kwargs):
        obon = Obon.objects.get(user_id=request.user.id)
        context = {
            'obon' : obon
        }
        
        return render(request, 'foodstore.html', context)
    
    def post(self, request, *args, **kwargs):
        obon = Obon.objects.get(user_id=request.user.id)
        context = {}
        
        # リセットボタンの処理
        if('reset' in request.POST):
            obon.delete()
            obon = Obon.objects.create(user_id=request.user.id)
            
        # 買える物があるかチェック
        flag = 0
        for item_money in item_moneys.values():
            if(obon.money - item_money >= 0):  # 買えるものがあれば
                flag = 1
            
        if(flag == 0):  # 買えるものが無ければ戦闘画面へ
            context |= {
                'obon' : obon,
                'error' : '買える物がありません！',
                'battle' : "戦闘画面へ！"
            }
            return render(request, 'registration/index.html', context)

        # たこ焼き
        if('takoyaki' in request.POST):
            if(self.check_money(context, obon, 'takoyaki')):
                return render(request, 'registration/index.html', {'data_json': json.dumps(context)})
            
            context |= takoyaki
            context |= {'money':item_moneys['takoyaki'], 'flag' : 1}

            obon.money -= item_moneys["takoyaki"]
            obon.save()
            self.grow_up(obon, takoyaki)
        
        # りんご飴
        if('ringoame' in request.POST):
            if(self.check_money(context, obon, 'ringoame')):
                return render(request, 'registration/index.html', context)
            
            context |= ringoame
            context |= {'money':item_moneys['ringoame'], 'flag' : 1}
            
            obon.money -= item_moneys["ringoame"]
            obon.save()
            self.grow_up(obon, ringoame)
            
        # やきそば
        if('yakisoba' in request.POST):
            if(self.check_money(context, obon, 'yakisoba')):
                return render(request, 'registration/index.html', context)
            
            context |= yakisoba
            context |= {'money':item_moneys['yakisoba'], 'flag' : 1}
            
            obon.money -= item_moneys["yakisoba"]
            obon.save()
            self.grow_up(obon, yakisoba)
        
        # チョコバナナ
        if('tyokobanana' in request.POST):
            if(self.check_money(context, obon, 'tyokobanana')):
                return render(request, 'registration/index.html', context)
            
            context |= tyokobanana
            context |= {'money':item_moneys['tyokobanana'], 'flag' : 1}
            
            obon.money -= item_moneys["tyokobanana"]
            obon.save()
            self.grow_up(obon, tyokobanana)
        
        
        # --進化判定--
        # 銀のおぼん
        if(obon.weight > 10):
            obon.image = 'silver.jpg'
            obon.material = 'Silver'
            obon.save()
        
        # うるしのおぼん
        if(obon.motivation > 8):
            obon.image = 'urushi.jpg'
            obon.material = 'urushi'
            obon.save()


        context |= {
            'obon' : obon
        }
        return render(request, 'registration/index.html', context)


    def check_money(self, context, obon, item):
        if(obon.money - item_moneys[item] < 0):
            context |= {
                'obon': obon,
                'error':'所持金が足りません！'
            }
            return True
    
    def grow_up(self, obon, item):
        obon.size += item["size"]
        obon.wise += item["wise"]
        obon.weight += item["weight"]
        obon.motivation += item["motivation"]
        obon.save()
    