from django.urls import path

from report_hr_hiring.views import home , generate_report , report ,task_report ,timeperiod , hr_report, mainpage, Teamlead_report, Candidate_report,account_report

urlpatterns =[
  path('',home, name= 'home'),
  path('generate_report/',generate_report, name= 'generate_report'),
  path('report/',report, name= 'report'),
  path('task_report/',task_report, name= 'task_report'),
  path('timeperiod/',timeperiod, name= 'timeperiod'),
  path('hr_report/',hr_report, name= 'hr_report'),
  path('mainpage/',mainpage, name= 'mainpage'),
  path('Teamlead_report/',Teamlead_report, name= 'Teamlead_report'),
  path('Candidate_report/',Candidate_report, name= 'Candidate_report'),
  path('account_report/',account_report, name= 'account_report'),
  
]