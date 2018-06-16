from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking
# Create your views here.
API_KEY='a98885a5b35185f219cd35263a9a3a7db9196f24a9df7e12a740a9eec53741d4'

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')


        if text == "":
            menu_text = "CON Welcome to De Law, Kindly choose an option:\n"
            menu_text += "1. Get Lawyer\n"
            menu_text += "2. Get Legal Advice\n"
      
        elif text =="1":
            menu_text = "CON Choose the type of lawyer you want to talk to \n"
            menu_text += "1. Criminal law\n"
            menu_text += "2. Family Law\n"
            menu_text += "3. Co-orperate Law \n" 
            menu_text += "4. Civil rights Law \n"
            menu_text += "5. Labor Law  \n"


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
    