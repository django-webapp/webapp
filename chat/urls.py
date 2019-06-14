from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import ThreadView, InboxView

app_name = 'chat'
urlpatterns = [
    path('chat/', TemplateView.as_view(template_name="chat/base.html")),
    path("inbox/", InboxView.as_view()),
    re_path(r"^chat/(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]