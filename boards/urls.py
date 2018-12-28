from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views as account_views

from .views import new_topic, reply_topic, PostUpdateView, BoardListView, TopicListView, PostListView
from accounts import views as accounts_views

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
    path('boards/<int:pk>/', TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<topic_pk>/reply/', reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<topic_pk>/posts/<post_pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('reset/', auth_views.PasswordResetView.as_view(
    	template_name='password_reset.html',
    	email_template_name='password_reset_email.html',
    	subject_template_name='password_reset_subject.txt'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
    	template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    	template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
    	template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'), name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name='password_change_done'),
    path('settings/account/', account_views.UserUpdateView.as_view(), name='my_account'),
]