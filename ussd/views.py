from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking

# Create your views here.
api_key='a98885a5b35185f219cd35263a9a3a7db9196f24a9df7e12a740a9eec53741d4'
username='sandbox'
phoneNumber='+254724629599'
url='https://de-law.herokuapp.com/'
serviceCode='*384*23519#'

@csrf_exempt
def africastalking(request):
    # africastalking.initializing(username,api_key)
    # ussd = africastalking.USSD
    response = ""
    if request.method == 'POST':
        session_id = request.POST.get('sessionId', None)
        service_code = request.POST.get('serviceCode', None)
        phone_number = request.POST.get('phoneNumber', None)
        text = request.POST.get('text', None)
        print(session_id)
        

        if text == "":
            menu_text = "CON Welcome to De Law, Kindly choose an option:\n"
            menu_text += "1. Get Lawyer\n"
            menu_text += "2. Choose your price\n"
      
        elif text =="1":
            menu_text = "CON Choose the type of lawyer you want to talk to \n"
            menu_text += "1. Criminal law\n"
            menu_text += "2. Family Law\n"
            menu_text += "3. Co-orperate Law \n" 
            menu_text += "4. Civil rights Law \n"
            menu_text += "5. Labor Law  \n"


        elif text =="2":
            menu_text = "CON Please enter an amount"
                
        elif text =="1*1":
            
            time.sleep(2)
            
        elif text =="1*2":
            menu_text = "CON Select a lawyer"
        
        elif text =="1*3":
            menu_text = "CON Choose one of the following lawyers"
            menu_text += "1. Wesley Mutwiri\n"
            menu_text += "2. Peter Muturi\n"
            menu_text += "3. Risper Kemmy\n"
            menu_text += "4. Olamijin\n"

            time.sleep(2)

        elif text =="1*4":
            menu_text = "CON Choose one of the following lawyers"
            menu_text += "1. Wesley Mutwiri\n"
            menu_text += "2. Peter Muturi\n"
            menu_text += "3. Risper Kemmy\n"
            menu_text += "4. Olamijin\n"

            time.sleep(2)
        
        elif text =="1*5":
            menu_text = "CON Choose one of the following lawyers"
            menu_text += "1. Wesley Mutwiri\n"
            menu_text += "2. Peter Muturi\n"
            menu_text += "3. Risper Kemmy\n"
            menu_text += "4. Olamijin\n"

            time.sleep(2)

        elif text =="2*"+userResponse:
            client.publish("amaina/amount",userResponse)
            client.subscribe("amaina/amount")
            time.sleep(2)
            menu_text = "END Thank-you"

    return HttpResponse(response)
    