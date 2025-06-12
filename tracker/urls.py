from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/hod/', views.hod_dashboard, name='hod_dashboard'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
    path('assets/', views.view_assets, name='view_assets'),
    path('maintenance/<int:asset_id>/', views.log_maintenance, name='log_maintenance'),
    path('maintenance/', views.view_maintenance, name='view_maintenance'),
    path('export/overall/', views.export_overall_report, name='export_overall_report'),
    path('collect-static/', views.collect_static_view),
    path('run-migrations/', views.run_migrations),
]
