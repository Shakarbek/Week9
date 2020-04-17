from django.urls import path

# from api.views.views0 import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail, top_ten_vacancies
from api.views import company_list, company_detail, vacancy_list, vacancy_detail
from api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView
from api.views.view_generic import CompanyListAPIView, VacancyListAPIView, VacancyDetailAPIView

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns=[
    # path('companies', company_list),
    # path('companies/<int:company_id>/', company_detail),
    path('companies/<int:id>/vacancies/', CompanyListAPIView.as_view()),
    # path('vacancies', vacancy_list),
    # path('vacancies/<int:vacancy_id>/', vacancy_detail),

    path('vacancies', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),

    # path('vacancies/top_ten/', top_ten_vacancies)
    path('companies', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView),
    path('login',obtain_jwt_token)
]
