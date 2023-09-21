from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import DogInfo
from .forms import DogInfoForm
from django.views import View



# 앱 이름 설정 (이 부분은 일반적으로 views.py가 아닌, urls.py에서 설정합니다)
app_name = 'dogtag'

class DogInfoCreateView(CreateView):
    model = DogInfo
    form_class = DogInfoForm
    template_name = 'doginfo_form.html'
    success_url = reverse_lazy('dogtag:doginfo_list')
    
    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            return HttpResponse('<script type="text/javascript">alert("휴대폰 번호 형식은 \'010-1234-5678\'과 같은 형태로 입력하세요."); window.location.href="";</script>')

class DogInfoUpdateView(UpdateView):
    model = DogInfo
    form_class = DogInfoForm
    template_name = 'doginfo_form.html'
    success_url = reverse_lazy('dogtag:doginfo_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit_mode'] = True  # 플래그 설정
        return context

class DogInfoDeleteView(View):
    def post(self, request, *args, **kwargs):
        try:
            dog_info = DogInfo.objects.get(pk=kwargs['pk'])
            dog_info.delete()
            return JsonResponse({'status': 'success'})
        except DogInfo.DoesNotExist:
            return JsonResponse({'status': 'failed'}, status=400)


class DogInfoDetailView(DetailView):
    model = DogInfo
    template_name = 'doginfo_detail_view.html'

    
class DogInfoListView(ListView):
    model = DogInfo
    template_name = 'doginfo_list.html'
