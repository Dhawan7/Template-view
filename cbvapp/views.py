from django.shortcuts import render
from django.views.generic import View,TemplateView

class MyCBV(TemplateView):
    template_name= 'index.html'

    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        data['var1'] = "I am data variable 1"
        data['var2'] =100
        return data
