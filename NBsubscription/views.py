from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count
import numpy as np
import matplotlib.pyplot as plt

from user.models import User
from NBsubscription.models import NB
from rest_framework.views import APIView


class NB(APIView):
    def NB(self, request):
        sum_k = User.objects.filter(subscription='경향신문').aggregate(Count('subscription'))
        sum_j = User.objects.filter(subscription='중앙일보').aggregate(Count('subscription'))
        sum_y = User.objects.filter(subscription='연합뉴스').aggregate(Count('subscription'))

        prefer_L = [sum_k['subscription__count'], sum_j['subscription__count'], sum_y['subscription__count']]

        likepercent = []
        total_prefer = NB.objects.aggregate(Sum('sub_total'))

        for i in range(len(prefer_L)):
            likepercent.append(int(prefer_L[i]) / int(total_prefer['sub_total__sum']) * 100)

        newspaper = ['경향신문', '중앙일보', '연합뉴스']
        index = np.arange(len(newspaper))

        plt.bar(index, likepercent, color=['b', 'r', 'g'], width=0.7, alpha=0.3)
        plt.title('The number of newspaper broadcaster prefer')
        plt.xticks(index, newspaper)
        plt.yticks(likepercent)
        plt.xlabel('newspaper broadcaster')
        plt.ylabel('%')
        plt.ylim(0, 80)
        plt.savefig('newspaper_prefer.png')

        return render(request, "NBsubscription/Profile.html")

    # if __name__ == '__main__':
    # app.run(port=5556)