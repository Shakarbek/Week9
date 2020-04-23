import json

from django.shortcuts import render

from django.http.response import JsonResponse
from django.http import Http404
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.models import Company, Vacancy

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CompanySerializer, VacancySerializer

class CompanyListAPIView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data, )

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyDetailAPIView(APIView):
    def get_object(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        company =self.get_object(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    def put(self, request, company_id):
        company =self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    def delete(self, request, company_id):
        company =self.get_object(company_id)
        company.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method =='GET':
        companies= Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data )

    elif request.method =='POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})
        # raise Http404
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})

#
# @csrf_exempt
# def vacancy_list(request):
#     if request.method =='GET':
#         vacancies= Vacancy.objects.all()
#         serializer = VacancySerializer( vacancies, many=True)
#
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method =='POST':
#         request_body=json.loads(request.body)
#
#         serializer = VacancySerializer(data=request_body)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse({'error': serializer.errors})
#
# @csrf_exempt
# def vacancy_detail(request, vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#         # raise Http404
#     if request.method == 'GET':
#         serializer = VacancySerializer(vacancy)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         request_body = json.loads(request.body)
#         serializer = VacancySerializer(instance=vacancy, data=request_body)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse({'error': serializer.errors})
#
#     elif request.method == 'DELETE':
#         vacancy.delete()
#         return JsonResponse({'deleted': True})