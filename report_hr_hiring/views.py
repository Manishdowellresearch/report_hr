from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
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
        response = targeted_population('hr_hiring','tasks',  ['task_details'], 'life_time')
        all_tasks = [data['task_details'] for data in response['normal']['data'][0]]
        def find_candidate_tasks(candidate, task_list):
            tasks = []
            for task in task_list:
                if task['user'] == candidate:
                    tasks.append(task)
            if len(tasks) != 0:
                return tasks

            return {f"No task for {candidate} found": f"No task for {candidate} found"}
        candidate_task = find_candidate_tasks(candidate_name, all_tasks)
        return render(request, 'report.html',context={"candidate_task":candidate_task})
    else:
        return redirect('home')
        #response = targeted_population('hr_hiring','tasks',  ['task_details'], 'life_time')


@csrf_exempt
def report(request):
    response = targeted_population('hr_hiring','candidate_view',  ['candidate_data'], 'last_1_day')
    print(response)
    candidate=[]
    for i in response['normal']['data'][0]:
        candidate.append(i['candidate_data']['applicant'])
    return JsonResponse({"candidate":candidate})
    
@csrf_exempt
def task_report(request):
    if request.method == 'POST':
        candidate_name =request.POST['candidate_name']
        response = targeted_population('hr_hiring','tasks',  ['task_details'], 'life_time')
        all_tasks = [data['task_details'] for data in response['normal']['data'][0]]
        def find_candidate_tasks(candidate, task_list):
            tasks = []
            for task in task_list:
                if task['user'] == candidate:
                    tasks.append(task)
            if len(tasks) != 0:
                return tasks

            return {f"No task for {candidate} found": f"No task for {candidate} found"}
        candidate_task = find_candidate_tasks(candidate_name, all_tasks)
        return JsonResponse({"candidate_task":candidate_task})

   