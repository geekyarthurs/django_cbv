from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import School, Students
from django.urls import reverse, reverse_lazy
# Create your views here.

# class CBView(View):
#     def get(self, request):
#         return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "I am injected!"
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    #school_list
    model = School
    template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School
    template_name = 'basic_app/basic_app_school_form.html'


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School
    template_name = 'basic_app/basic_app_school_form.html'


class SchoolDeleteView(DeleteView):
    model = School

    template_name = 'basic_app/school_confirm_delete.html'
    success_url = reverse_lazy("basic_app:list")
