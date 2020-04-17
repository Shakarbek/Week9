from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from api.models import Company, Vacancy
from api.serializers import CompanyWithVacanciesSerializer, VacancySerializer

class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacanciesSerializer
    # permission_classes = (IsAuthenticated)

class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer