from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from user.forms import RegisterForm, BillingAddressForm, BillingInfoForm


@login_required
def index(request):

    return render(request, 'user/index.html', {})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect("/")
        else:
            return HttpResponseNotFound("Failed to log in")

    return render(request, 'user/user_login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return redirect("/user/login")


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
    else:
        form = RegisterForm()

    return render(request, 'user/user_register.html', {"form": form})


@login_required
def billing_address(request):
    edit_address = request.GET.get('edit_address', None)
    edit_form = None

    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user_id = request.user.id
            if edit_address:
                form_data.id = int(edit_address)
            form_data.save()
            return redirect('billing_address')
    form = BillingAddressForm()
    user_addresses = request.user.userbillingaddress_set.all()

    if edit_address:
        edit_address = int(edit_address)
        edit_form = BillingAddressForm(instance=request.user.userbillingaddress_set.get(id=edit_address))

    return render(request, 'user/billing_address.html', {
        "user_addresses": user_addresses,
        "form": form,
        "edit_address": edit_address,
        "edit_form": edit_form
    })


@login_required
def delete_billing_address(request, billing_address_id):
    query = request.user.userbillingaddress_set.filter(id=billing_address_id)
    if query.exists():
        query.first().delete()

    return redirect('billing_address')


@login_required
def billing(request):
    edit_billing = request.GET.get('edit_billing', None)
    edit_form = None

    if request.method == 'POST':
        form = BillingInfoForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user_id = request.user.id
            if edit_billing:
                form_data.id = int(edit_billing)
            form_data.save()
            return redirect('billing')
    form = BillingInfoForm()
    user_billings = request.user.userbillinginfo_set.all()

    if edit_billing:
        edit_billing = int(edit_billing)
        edit_form = BillingInfoForm(instance=request.user.userbillinginfo_set.get(id=edit_billing))

    return render(request, 'user/billing.html', {
        "user_billings": user_billings,
        "form": form,
        "edit_billing": edit_billing,
        "edit_form": edit_form
    })


@login_required
def delete_billing(request, billing_id):
    query = request.user.userbillinginfo_set.filter(id=billing_id)
    if query.exists():
        query.first().delete()

    return redirect('billing')


@login_required
def rented_lockers(request):
    return render(request, 'user/rented_lockers.html', {})