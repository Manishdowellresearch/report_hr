from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .dowellpopulationfunction import targeted_population
# Create your views here.
@csrf_exempt
def home(request):
    response = targeted_population('hr_hiring','candidate_view',  ['candidate_data'], 'life_time')
    candidate=[]
    for i in response['normal']['data'][0]:
        candidate.append(i['candidate_data']['applicant'])
    return render(request,'home.html',context={"candidate":candidate})


@csrf_exempt
def generate_report(request):
    if request.method == 'POST':
        candidate_name =request.POST['candidate_name']
        return HttpResponse(candidate_name)
    else:
        return HttpResponse("ok")
        #response = targeted_population('hr_hiring','tasks',  ['task_details'], 'life_time')



