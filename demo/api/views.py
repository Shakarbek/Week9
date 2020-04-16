from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.http import Http404

def company_list(request):
    if request.method=='GET':
        companies = Company.objects.all()
        # products = Product.objects.filter(price__gte=1000).order_by('-price')
        companies_json=[company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)

def vacancy_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
        # raise Http404
    if request.method == 'GET':
        return JsonResponse(company.to_json())

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
        # raise Http404
    return JsonResponse({'data': f'vacancies of company: {company_id}'})


def vacancy_list(request):
    if request.method=='GET':
        vacancies = Vacancy.objects.all()
        # products = Product.objects.filter(price__gte=1000).order_by('-price')
        vacancies_json=[vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

def company_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
        # raise Http404
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

def top_ten_vacancies(request):
    if request.method=='GET':
        vacancies = Vacancy.objects.order_by('-salary').limit(10)
        vacancies_json=[vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)