from django.urls import path

from report_hr_hiring.views import home , generate_report , report ,task_report

urlpatterns =[
  path('',home, name= 'home'),
  path('generate_report/',generate_report, name= 'generate_report'),
  path('report/',report, name= 'report'),
  path('task_report/',task_report, name= 'task_report'),
]