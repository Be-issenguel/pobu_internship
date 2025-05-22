from django.shortcuts import render
from django.views.generic import View
from datetime import datetime

# Create your views here.
class HomeView(View):

    def get(self, request):
        now = datetime.now().strftime("%Y")
        return render(request=request, template_name='frontend/home.html', context={'current_date': now})
