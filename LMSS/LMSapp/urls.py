from django.urls import re_path
from LMSapp import views


urlpatterns = [
    

    re_path(r'^Issue_Book$',views.IssueApi),
    re_path(r'^Issue_Book/([0-9]+)$',views.IssueApi),

    re_path(r'^Return_Book$',views.ReturnApi),
    re_path(r'^Return_Book/([0-9]+)$',views.ReturnApi),

    re_path(r'^AB_Book$',views.ABApi),
    re_path(r'^AB_Book/([0-9]+)$',views.ABApi),

    re_path(r'^Newadd_Book$',views.NewaddApi),
    re_path(r'^Newadd_Book/([0-9]+)$',views.NewaddApi),


]
