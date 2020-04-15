from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib import messages
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as login_process
import stripe

stripe.api_key = 'sk_test_uWYsVHakqbXSWexgxfIdA3qM00NhGb6G2X'


@login_required(login_url='/login')
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    context = {'username': username}
    return render(request, 'example/index.html', context)


@login_required(login_url='/login')
def profile(request):
    return render(request, 'example/profile.html')


def register(request):
    if request.method == 'POST':

        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'example/register.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login_process(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, 'The username and/or password you specified are not correct.')
            return redirect('login')
    else:
        return render(request, 'example/login.html')

@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    return redirect('login')


# def login(request):
#     if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         auth_login(request, user)
    #         return redirect('index')
    #     else:
    #         messages.add_message(request, messages.INFO, 'The username and/or password you specified are not correct.')
    #         return redirect('login')
    # else:
    #     return render(request, '/login.html')

def index1(request):
    return render(request, 'stripe/index1.html')


def charge(request):
    # amount = 10

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(

            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description="Donation"
            )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'stripe/success.html', {'amount': amount})