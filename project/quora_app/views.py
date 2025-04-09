from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, QuestionForm, AnswerForm
from .models import Question, Answer, Like

class RegisterView(View):
    """
    This view handles user registration functionality
    """
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        try:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('question_list')
            return render(request, 'register.html', {'form': form})
        except Exception as e:
            return render(request, 'register.html', {'form': form, 'error': str(e)})

class LoginView(View):
    """
    This view handles user login functionality
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        try:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('question_list')
            return render(request, 'login.html', {'form': form})
        except Exception as e:
            return render(request, 'login.html', {'form': form, 'error': str(e)})

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    """
    This view handles logout functionality
    """
    def get(self, request):
        try:
            logout(request)
            return redirect('login')
        except Exception as e:
            return render(request, 'login.html', {'error': str(e)})

@method_decorator(login_required, name='dispatch')
class QuestionListView(View):
    """
    This view displays a list of all questions
    """
    def get(self, request):
        try:
            questions = Question.objects.all()
            return render(request, 'question_list.html', {'questions': questions})
        except Exception as e:
            return render(request, 'question_list.html', {'error': str(e)})

@method_decorator(login_required, name='dispatch')
class PostQuestionView(View):
    """
    This view allows users to post a new question
    """
    def get(self, request):
        form = QuestionForm()
        return render(request, 'post_question.html', {'form': form})

    def post(self, request):
        try:
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.user = request.user
                question.save()
                return redirect('question_list')
            return render(request, 'post_question.html', {'form': form})
        except Exception as e:
            return render(request, 'post_question.html', {'form': form, 'error': str(e)})

@method_decorator(login_required, name='dispatch')
class QuestionDetailView(View):
    """
    This view displays a question's details and allows users to post answers
    """
    def get(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            answers = Answer.objects.filter(question=question)
            form = AnswerForm()
            return render(request, 'question_detail.html', {
                'question': question,
                'answers': answers,
                'form': form
            })
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        except Exception as e:
            return render(request, 'question_detail.html', {'error': str(e)})

    def post(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            answers = Answer.objects.filter(question=question)
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.user = request.user
                answer.question = question
                answer.save()
                return redirect('question_detail', question_id=question.id)
            return render(request, 'question_detail.html', {
                'question': question,
                'answers': answers,
                'form': form
            })
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        except Exception as e:
            return render(request, 'question_detail.html', {
                'question': question,
                'answers': answers,
                'form': form,
                'error': str(e)
            })

@method_decorator(login_required, name='dispatch')
class LikeAnswerView(View):
    """
    This view allows users to like or unlike an answer
    """
    def get(self, request, answer_id):
        try:
            answer = Answer.objects.get(id=answer_id)
            like, created = Like.objects.get_or_create(user=request.user, answer=answer)
            if not created:
                like.delete()
            return redirect('question_detail', question_id=answer.question.id)
        except Answer.DoesNotExist:
            raise Http404("Answer does not exist")
        except Exception as e:
            return redirect('question_detail', question_id=answer.question.id)

@method_decorator(login_required, name='dispatch')
class DeleteQuestionView(View):
    """
    This view allows users to delete their own questions
    """
    def get(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            if question.user != request.user:
                raise Http404("You are not authorized to delete this question")
            question.delete()
            return redirect('question_list')
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        except Exception as e:
            return render(request, 'question_list.html', {'error': str(e)})