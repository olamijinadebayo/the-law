from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        if text == "":
            menu_text = "CON Welcome to KPLC prepaid, please choose an option:\n"
            menu_text += "1. Check my Account information\n"
            menu_text += "2. Top-Up my balance\n"
      
        elif text =="1":
            menu_text = "CON Choose the account information that you want to view \n"
            menu_text += "1. My Token balance\n"
            menu_text += "2. My Account number \n"

        elif text =="2":
            menu_text = "CON Please enter the amount"
                
        elif text =="1*1":
            token = random.randrange(16,38)
            menu_text = "END Your Token balance is: "+ str(token)
            client.publish("amaina/token",token)
            send_sms("Your remaining tokens are: ", token)
            time.sleep(2)
            
        elif text =="1*2":
            menu_text = "END Your account number is ACOO10SWO2101."
        
        elif text =="2*"+userResponse:
            client.publish("amaina/amount",userResponse)
            client.subscribe("amaina/amount")
            send_sms("Thank you the amount paid in is: ", userResponse)
            time.sleep(2)
            menu_text = "END Thank-you"

    return HttpResponse(response)