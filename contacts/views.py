from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact_now(request):
	return redirect('home')
def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		slug = request.POST['listing_slug']
		product_title = request.POST['product_title']
		name = request.POST['full_name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message'] 
		user_id = request.POST['user_id']
		seller_email = request.POST['seller_email']
		# check if user has made qnquert alread
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
			if has_contacted:
				messages.error(request,'You hgave already made enquery for this listing')
				return redirect('/'+listing_id+slug)
				
		contact = Contact(product_title=product_title, listing_id=listing_id,listing_slug=slug, name=name,
        	email=email, phone=phone, message=message, user_id=user_id)
		contact.save()

		messages.success(request,'Your inquery has been send you will be notified soon')	
		return redirect('/'+listing_id+slug)

		# # return redirect('/')