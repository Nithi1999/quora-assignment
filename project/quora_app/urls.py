from django.urls import path
from .views import RegisterView, LoginView, LogoutView, QuestionListView, PostQuestionView, QuestionDetailView, LikeAnswerView, DeleteQuestionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', QuestionListView.as_view(), name='question_list'),
    path('post-question/', PostQuestionView.as_view(), name='post_question'),
    path('question/<int:question_id>/', QuestionDetailView.as_view(), name='question_detail'),
    path('like/<int:answer_id>/', LikeAnswerView.as_view(), name='like_answer'),
    path('delete-question/<int:question_id>/', DeleteQuestionView.as_view(), name='delete_question'),
]