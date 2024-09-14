from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
import pandas as pd
from .models import BusinessData, Expenditure
from .ml_models import create_business_performance_model, predict_performance
from .data_analysis import generate_performance_chart

# View for generating business performance predictions
@login_required
def performance_prediction(request):
    data = BusinessData.objects.all().values('capital', 'daily_sales', 'profit_loss')
    data = pd.DataFrame.from_records(data)

    # Train the model
    model = create_business_performance_model(data)

    # Predict performance for a specific example (dummy values)
    prediction = predict_performance(model, capital=10000, daily_sales=5000)

    return render(request, 'performance.html', {'prediction': prediction})

# View for generating performance chart
@login_required
def performance_chart_view(request):
    data = BusinessData.objects.all().values('date', 'profit_loss')
    data = pd.DataFrame.from_records(data)

    # Generate chart
    chart = generate_performance_chart(data)

    return render(request, 'performance_chart.html', {'chart': chart})

# Payment processing function
def process_payment(payment_method, amount, user):
    # Implement payment processing logic here
    if payment_method == 'credit_card':
        print(f"Processing credit card payment of ${amount} for {user}")
    elif payment_method == 'paypal':
        print(f"Processing PayPal payment of ${amount} for {user}")
    else:
        print("Unsupported payment method")
    
    # Assuming payment is successful
    return True

# View for handling payments
@login_required
def make_payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        amount = request.POST.get('amount')
        user = request.user

        # Process payment
        response = process_payment(payment_method, amount, user)

        return render(request, 'payment_result.html', {'response': response})
    return render(request, 'payment.html')

# User type checks
def is_entrepreneur(user):
    return user.profile.user_type == 'Entrepreneur'

def is_revenue_officer(user):
    return user.profile.user_type == 'RevenueOfficer'

def is_investor(user):
    return user.profile.user_type == 'Investor'

# Dashboard views
@login_required
@user_passes_test(is_entrepreneur)
def entrepreneur_dashboard(request):
    return render(request, 'entrepreneur_dashboard.html')

@login_required
@user_passes_test(is_revenue_officer)
def revenue_officer_dashboard(request):
    return render(request, 'revenue_officer_dashboard.html')

@login_required
@user_passes_test(is_investor)
def investor_dashboard(request):
    return render(request, 'investor_dashboard.html')

# Expenditures management views
@login_required
def expenditures(request):
    expenditures = Expenditure.objects.filter(owner=request.user.profile)
    return render(request, 'expenditures.html', {'expenditures': expenditures})

@login_required
def add_expenditure(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        Expenditure.objects.create(owner=request.user.profile, description=description, amount=amount, date=date)
        return redirect('expenditures')
    return render(request, 'add_expenditure.html')

@login_required
def delete_expenditure(request, expenditure_id):
    expenditure = get_object_or_404(Expenditure, id=expenditure_id, owner=request.user.profile)
    expenditure.delete()
    return redirect('expenditures')

# Basic views
def loading_page(request):
    return render(request, 'loading.html')

def language_selection(request):
    return render(request, 'language_selection.html')

def sign_in(request):
    return render(request, 'sign_in.html')

@login_required
def home(request):
    user_type = request.user.profile.user_type
    return render(request, 'home.html', {'user_type': user_type})

@login_required
def profile(request):
    return render(request, 'profile.html', {'profile': request.user.profile})

@login_required
def inbox(request):
    return render(request, 'inbox.html')

@login_required
def tax_reports(request):
    return render(request, 'tax_reports.html')

def about_us(request):
    return render(request, 'about_us.html')

def chatbot(request):
    return render(request, 'chatbot.html')
