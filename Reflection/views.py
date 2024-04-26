from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Journal
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'Reflection/index.html'


def journal_list(request):
    journals = Journal.objects.filter(owner=request.user)
    context = {
        'journals': journals
    }

    return render(request, 'Reflection/journal_list.html', context)


class JournalCreateView(CreateView):
    model = Journal
    success_url = reverse_lazy('journal-list')
    fields = ['title', 'notes', 'image', 'created_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user  # owner - logged in user itself
        return super().form_valid(form)


def Journal_details(request, id):
    Journal_detail = get_object_or_404(Journal, id=id,)
    context = {
        "journal": Journal_detail
    }

    return render(request, 'Reflection/details.html', context)


class JournalUpdateView(UpdateView):
    model = Journal
    success_url = reverse_lazy('journal-list')
    fields = ['title', 'notes', 'image', 'created_date']

    def get_form(self):
        form = super(JournalUpdateView, self).get_form()
        form.instance.owner = self.request.user  # owner - logged in user itself
        return form


class JournalDeleteView(DeleteView):
    model = Journal
    success_url = reverse_lazy('journal-list')
