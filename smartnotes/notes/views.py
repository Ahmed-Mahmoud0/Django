from .models import Notes
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = "notes/notes_list.html"
    context_object_name = 'notes'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    template_name = "notes/notes_detail.html"
    context_object_name = 'note'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = 'notes/notes_delete.html'
    context_object_name = 'note'
