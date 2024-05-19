from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

class TaskView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
    