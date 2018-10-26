from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
     path('PostApi/', views.PostViewList.as_view()),
     path('PostApi/<int:pk>', views.PostViewDetails.as_view()),
     path('AdmitCardsApi/', views.AdmitCardsViewList.as_view()),
     path('AdmitCardsApi/<int:pk>', views.AdmitCardsViewDetails.as_view()),
     path('ResultApi/', views.ResultViewList.as_view()),
     path('EmailsApi/', views.EmailsViewList.as_view()),
     path('ResultApi/<int:pk>', views.ResultViewDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
