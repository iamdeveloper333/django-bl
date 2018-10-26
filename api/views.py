from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse,Http404
from api.models import Post,AdmitCards,Result,Emails
from rest_framework import generics
from api.serializers import PostSerialiazers
from api.serializers import AdmitCardsSerialiazers
from api.serializers import ResultSerialiazers
from api.serializers import EmailsSerialiazers

from api.filters import (
    PostFilter,AdmitCardsFilter,ResultFilter
)



# from api.filters import PostFilter

# Create your views here.

class PostViewList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

class PostViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers

class AdmitCardsViewList(generics.ListCreateAPIView):
    queryset = AdmitCards.objects.all()
    serializer_class = AdmitCardsSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = AdmitCardsFilter

class EmailsViewList(generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerialiazers

class AdmitCardsViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdmitCards.objects.all()
    serializer_class = AdmitCardsSerialiazers

class ResultViewList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = ResultFilter

class ResultViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerialiazers
