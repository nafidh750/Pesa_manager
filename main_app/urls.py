from django.urls import path
from . import views

urlpatterns = [
    # Basic pages
    path('', views.loading_page, name='loading'),
    path('language/', views.language_selection, name='language_selection'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('tax-reports/', views.tax_reports, name='tax_reports'),
    path('about-us/', views.about_us, name='about_us'),
    path('chatbot/', views.chatbot, name='chatbot'),

    # Dashboard pages
    path('entrepreneur-dashboard/', views.entrepreneur_dashboard, name='entrepreneur_dashboard'),
    path('revenue-officer-dashboard/', views.revenue_officer_dashboard, name='revenue_officer_dashboard'),
    path('investor-dashboard/', views.investor_dashboard, name='investor_dashboard'),

    # Performance views
    path('performance-prediction/', views.performance_prediction, name='performance_prediction'),
    path('performance-chart/', views.performance_chart_view, name='performance_chart'),

    # Payment views
    path('make-payment/', views.make_payment, name='make_payment'),

    # Expenditures management
    path('expenditures/', views.expenditures, name='expenditures'),
    path('expenditures/add/', views.add_expenditure, name='add_expenditure'),
    path('expenditures/delete/<int:expenditure_id>/', views.delete_expenditure, name='delete_expenditure'),
]
