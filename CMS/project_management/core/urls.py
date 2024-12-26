from django.urls import path
from . import views

urlpatterns = [

    path('clients/', views.client_list, name='client_list'),
    path('clients/register/', views.register_client, name='register_client'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/add_project/', views.add_project, name='add_project'),
    path('user/projects/', views.projects_for_user, name='projects_for_user'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),  # Edit project
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),  # Delete project
    path('projects/', views.project_list, name='project_list'),

    
]
