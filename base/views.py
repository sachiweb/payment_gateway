from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    data={}
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        client = razorpay.Client(
            auth=("rzp_test_P7LGA5hhnucq5m", "I07NCl1t4b9aZY3UdP1DcmlL"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        data={
            'amount':amount
        }
    return render(request, 'index.html',data)

@csrf_exempt
def success(request):
    return render(request, "success.html")
