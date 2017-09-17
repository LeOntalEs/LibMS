from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import make_aware

from docmanager.models import *
from docmanager.forms import *

# Create your views here.
class DocumentListView(ListView):
    model = Document
    context_object_name = "documents"
    template_name = 'doc_list.html'

class AddDocumentView(LoginRequiredMixin, FormView):
    template_name = 'add_doc.html'
    form_class = DocumentForm

    def form_valid(self, form):
        doc = form.save(commit=False)
        author = form.cleaned_data['author']
        date = form.cleaned_data['release_date']
        doc.author = Author.objects.get(pk=author.id)
        doc.release_date = date
        doc.save()
        return HttpResponse('Add Complete, Thank you.', status=200)

def hello(request):
    return HttpResponse('Hello World', status=200)


#
# FBV Style
#
# def doc_list(request):
#     docs = Document.objects.all()
#     return render(request, 'doc_list.html', {'documents': docs})
# def add_doc(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST)
#         if form.is_valid():
#             doc = form.save(commit=False)
#             author = form.cleaned_data['author']
#             doc.author = Author.objects.get(pk=author.id)
#             doc.save()
#             return HttpResponse('Add Complete, Thank you.', status=200)
#         else:
#             return HttpResponse('Invalid input format', status=400)
#     else:
#         form = DocumentForm()
#         context = {'form':form}
#         return render(request, 'add_doc.html', context)