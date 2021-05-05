
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order,Account
# from ..social_login.settings import SOCIAL_AUTH_FACEBOOK_SCOPE
@login_required
def home(request):
	ctx = {
		'user': request.user
	}
	print('..............................................................')
	# print(request.user.email)
	if request.user.is_authenticated:
		ctx.update({
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'email': request.user.email
		})
		print(ctx)
	if ctx['email']:
		request.session['email']=ctx['email']
		print(request.session['email'])
		try:
			Account.objects.get(email=request.session['email'])
		except:
			ac=Account.objects.create(email=request.session['email'])
			ac.save()

	return render(request,'home.html')


def order(request):

	try:
		email_id = request.session['email']
		obj=Order.objects.get(email=email_id)
		print("hre")
		print(obj)
		data={'order':obj.order_name,'status':obj.status}
		return render (request,'order.html',{'data':data})
	except:
		data = {'order': "No order found"}
		return render(request,'order.html',{'data':data})