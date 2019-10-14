from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question
from .forms import AnswerForm

class QuestionView(LoginRequiredMixin ,DetailView):
    model = Question
    content_object_name = 'question'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields =['title', 'description']

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk        
        return super().form_valid(form)

@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('post_detail', pk = question.pk)
    else:
        form = AnswerForm()
    return render(request, 'posts/add_answer.html', {'form': form})


class QuestionListView(LoginRequiredMixin ,ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date']


