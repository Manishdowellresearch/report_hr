from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .dowellpopulationfunction import targeted_population
import json
# Create your views here.
@csrf_exempt
def home(request):
    response = targeted_population('hr_hiring','candidate_view',  ['candidate_data'], 'life_time')
    candidate=[]
    for i in response['normal']['data'][0]:
        candidate.append(i['candidate_data']['applicant'])
    print(candidate)
    return render(request,'home.html',context={"candidate":candidate})


@csrf_exempt
def generate_report(request):
    if request.method == 'POST':
        candidate_name =request.POST['candidate_name']
        print(candidate_name)
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
    response = targeted_population('hr_hiring','candidate_view',  ['candidate_data'], 'life_time')
    print(response)
    candidate=[]
    for i in response['normal']['data'][0]:
        candidate.append(i['candidate_data']['applicant'])

    return JsonResponse({"candidate":candidate})

@csrf_exempt
def timeperiod(request):
    timeperiod= ['custom' , 'last_1_day' , 'last_30_days' , 'last_90_days' , 'last_180_days' , 'last_1_year' , 'life_time']
    return JsonResponse({"time":timeperiod})

@csrf_exempt
def task_report(request):
    if request.method == 'POST':
        candidate_name =request.POST['candidate_name']
        time_period = request.POST['time_period']
        response = targeted_population('hr_hiring','tasks',  ['task_details'], time_period)
        all_tasks = [data['task_details'] for data in response['normal']['data'][0]]
        def find_candidate_tasks(candidate, task_list):
            tasks = []
            for task in task_list:
                if task['user'] == candidate:
                    tasks.append(task)
            if len(tasks) != 0:
                return tasks

            return tasks
        candidate_task = find_candidate_tasks(candidate_name, all_tasks)
        return JsonResponse({"candidate_task":candidate_task})

   


@csrf_exempt
def hr_report(request):
    timeperiod= ['custom' , 'last_1_day' , 'last_30_days' , 'last_90_days' , 'last_180_days' , 'last_1_year' , 'life_time']

    if request.method == 'POST':
        Time_period = request.POST.get('Timeperiod')
        print(Time_period)
        response = targeted_population('hr_hiring','hr_view',  ['application_details'], Time_period)
        if response['normal']['is_error'] == True :
              return render(request, 'hr_report.html',context={"timeperiod":timeperiod})
        else:
         Task_detail = [data['application_details'] for data in response['normal']['data'][0]]
        def find_tasks_status(task_detail):
            shortlisted = []
            selected  = []
            teamlead_hire = []
            hired = []
            for task in task_detail:
                if task['status'] == "shortlisted":
                     shortlisted.append(task)
                elif task['status'] == "selected":
                     selected.append(task)
                elif task['status'] == "teamlead_hire":
                          teamlead_hire.append(task)
                else:
                          hired.append(task)
         
            total_shorlisted_candidate = len(shortlisted)
            total_selected_candidate = len(selected)
            total_teamlead_hire_candidate = len(teamlead_hire)
            total_hired_candidate = len( hired)
        
            data =[total_shorlisted_candidate , total_selected_candidate, total_teamlead_hire_candidate, total_hired_candidate]
           
            return data
        Task_status = find_tasks_status(Task_detail)
        print(Task_status)
        return JsonResponse({"Task_status":  Task_status})
        # return HttpResponse(json.dumps(Task_status ), content_type="application/json")
        # return render(request, 'hr_report.html',context={"timeperiod":timeperiod ,"data":Task_status })
    else:
           return render(request, 'hr_report.html')



