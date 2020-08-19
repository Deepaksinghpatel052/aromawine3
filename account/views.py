from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.urls import reverse_lazy
from account.forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from wineproject import settings
from django.contrib.auth.models import User,auth
import email.message
from django.contrib import messages
import smtplib


from django.http import HttpResponseRedirect,JsonResponse
import json
import requests
# Create your views here. #


def test_data(request):
	text = "this is test messsage for {name} and it's screen chhange"
	message = text.replace("{name}", "apples")
	return HttpResponse(message)



class AccountCraetLoginView(generic.TemplateView):
	form_class = SignUpForm
	template_name = "web/account/create_login.html"

	def get(self, request, *args, **kwargs):
		return render(request,self.template_name, {'form': self.form_class,'Page_title':"Account-Create & Login"})

	def post(self, request, *args, **kwargs):
		if "password2" in self.request.POST:
			form = self.form_class(request.POST)
			# captcha start
			client_key = request.POST['g-recaptcha-response']
			secretkey = '6LffT64ZAAAAANAdvYYGdfWW6FA1PdQxYK_IkgG5'

			capthchaData = {
				'secret':secretkey,
				'response': client_key
			}
			r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
			response = json.loads(r.text)
			varify = response['success']

			# captcha end
			if varify:
				if form.is_valid():
					form.save()
					messages.info(request,"account Created Successfuly.")
					success_url = reverse_lazy('account')
				else:
					messages.error(request, form.errors)
			else:
				messages.error(request, "Recaptcha is incorrect.")
			return render(request, self.template_name, {'form': form})
		else:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				if user.is_superuser:
					messages.error(request, "This login area is not used for superadmin.")
				else:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect('/user/dashboard/')
					else:
						messages.error(request, "Inactive user.")
			else:
				messages.error(request, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
			return render(request, self.template_name, {'form': self.form_class})


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")





@csrf_exempt
def send_forgate_password_link(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        # return JsonResponse({"status": "0", "message": user_email})

        if User.objects.filter(email=user_email).exists():
            data = User.objects.get(email=user_email)
            user_id = data.id

            # user_data = Ar_user.objects.get(user_id=user_id)
            name=data.first_name
            ###########################
            email_content = '<html> <head> <meta http-equiv="Content-Type" content="text/html; charset=euc-jp"> <meta name="viewport" content="width=device-width"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="x-apple-disable-message-reformatting"> <title>Agile | Password Reset</title> <style> html, body {background-color: #fff!important; margin: 0 auto !important; padding: 0 !important; height: 100% !important; width: 100% !important; color:#888!important; } .email-container{max-width: 600px!important; margin: 0 auto!important; } * {-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; } div[style*="margin: 16px 0"] {margin: 0 !important; } table, td {mso-table-lspace: 0pt !important; mso-table-rspace: 0pt !important; } table { width: 100%; border-spacing: 0 !important; border-collapse: collapse !important; table-layout: fixed !important; margin: 0 auto !important; } img {-ms-interpolation-mode:bicubic; } a {text-decoration: none!important; } *[x-apple-data-detectors], .unstyle-auto-detected-links *, .aBn {border-bottom: 0 !important; cursor: default !important; color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; } @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {u ~ div .email-container {min-width: 320px !important; } } @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {u ~ div .email-container {min-width: 375px !important; } } @media only screen and (min-device-width: 414px) {u ~ div .email-container {min-width: 414px !important; } } </style> </head> <body> <div class="email-container"> <table style="border-bottom: 2px solid #c52241; "> <tr> <td> <h2 style="color:#c52241; padding-top: 62px; margin-bottom: 0px;">Password Reset</h2> </td> <td> <img src="'+ settings.BASE_URL +'/static/web/assets/image/wine-logo.svg" style="width: 60%; float: right;"> </td> </tr> </table> <table style="color: #000;font-size: 20px;"> <tr> <td style="padding: 10px 0px;">Dear '+ name +',</td> </tr> <tr> <td style="padding: 10px 0px;">Seems like you forgot your password for AROMA OF WINE Platform. If it is True, Please click below to reset your password.</td> </tr> <tr> <td style="padding: 10px 0px;text-align:center;"> <button style="padding: 10px 45px;background-color: #000;border-radius: 10px;border: none;font-size:20px;color: #fff;"> <a href="'+ settings.BASE_URL +'" style="color: #fff; text-decoration: none;">Reset Password</a></button> </td> </tr> <tr> <td style="padding: 10px 0px;">If you did not forget your password, you can safely ignore this email.</td> </tr> </table> <table style="border-top: 1px solid #000; color: #000; font-size: 20px;"> <tr> <td style="font-weight: bold; padding-top: 30px;">Thank you for Joining!</td> </tr> <tr> <td style="font-weight: bold;padding-bottom: 30px;">The AROMA OF WINE Team</tr> </table> <table style="background-color: #f2f2f2; font-size: 20px;"> <tr> <td style="padding: 35px 30px; text-align: center;">DigiMonk Technologies, Software Technology Parks Of India Gwalior, Madhya Pradesh 474005</td> </tr> </table> </div> </body> </html>'
            msg = email.message.Message()
            msg['Subject'] = 'Forgot Password'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = user_email
            password = settings.EMAIL_HOST_PASSWORD
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            return JsonResponse({"status": "0", "message": user_id})
            ############################

        return JsonResponse({"status": "0", "message": 'user_email !'})



