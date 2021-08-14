from django.views import View
from django.shortcuts import render,redirect
from ..models import Obon

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
                'battle' : "戦闘画面へ！"
            }
            return render(request, 'registration/index.html', context)
                
                
        if('takoyaki' in request.POST):
            if(self.check_money(context, obon, 'takoyaki')):
                return render(request, 'registration/index.html', context)
                
            obon.weight += 1
            obon.money -= item_moneys['takoyaki']
            obon.save()
        
        if('ringoame' in request.POST):
            if(self.check_money(context, obon, 'ringoame')):
                return render(request, 'registration/index.html', context)
            
            obon.motivation += 1
            obon.money -= 150
            obon.save()
        
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
                    'obon' : obon,
                    'error' : "所持金が足りません！"
            }
            return True