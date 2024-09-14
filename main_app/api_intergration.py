import requests

# Function to integrate with payment methods
def process_payment(payment_method, amount, user):
    api_endpoints = {
        'TigoPesa': 'https://api.tigo.com/v1/payment',
        'AirtelMoney': 'https://api.airtel.com/v1/payment',
        'MPesa': 'https://api.safaricom.co.ke/mpesa/v1/payment',
        'HaloPesa': 'https://api.halotel.co.tz/halopesa/v1/payment',
        'NMBBank': 'https://api.nmb.com/v1/payment',
        'CRDBBank': 'https://api.crdb.com/v1/payment'
    }

    if payment_method not in api_endpoints:
        return "Payment method not supported"

    url = api_endpoints[payment_method]
    payload = {
        'amount': amount,
        'user_id': user.id,
        'user_name': user.username
    }

    response = requests.post(url, json=payload)
    return response.json()

# Function to integrate with TRA for tax management
def fetch_tax_data(user):
    url = 'https://api.tra.go.tz/v1/tax'
    payload = {'user_id': user.id}
    
    response = requests.get(url, params=payload)
    return response.json()

def process_payment(payment_data):
    # Implement payment processing logic here
    return "Payment processed"

def fetch_tax_data():
    # Implement logic to fetch tax data here
    return {"tax": 1000, "status": "paid"}
