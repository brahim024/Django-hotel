from django.shortcuts import render ,redirect
 from django.comtrib.auth.decorators import login_required
 from django.contrib import messages
 from .forms import ImageCreateForm
# Create your views here.
@login_required
def image_craete(request):
	if request.method=='POST':
		# now form is sent 
		form=ImageCreateForm(data=request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			new_item=form.save(commit=False)
			new_item.user=request.user
			new_item.save()
			messages.success(request,'Image added successfully')
			return redirect(new_item.get_absolut_url())

	else:
		form=ImageCreateForm(data=request.GET)
	return render(request,'create.html',{'section':'images','form':form})