from django.shortcuts import render

from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms import inlineformset_factory

from .forms import RequestForm, ProductForm, CustomerForm,ReqToRawForm

from .admin import UserCreationform, UserChangeForm

from .models import Customer, Product, RawBatch, ReqToRaw, Requesition, RawMaterial

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            e = request.POST.get('email')
            p = request.POST.get('password')

            user = authenticate(request, username=e,password=p)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        #context = {'form':form}
        return render(request, 'main/login.html')

def registerView(request):
    form = UserCreationform()
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationform(request.POST)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return render(request, 'main/register.html', context)

@login_required(login_url='/login/')
def indexView(request):
    
    reqs = Requesition.objects.order_by('status')
    paginator = Paginator(reqs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    pend = reqs.count()

    context = { 'pend':pend, 'reqs':page_obj}
    return render(request, 'main/index.html', context)


@login_required(login_url='/login/')
def createRequest(request):
    formset = RequestForm()
    reqs = Requesition.objects.order_by('status','Date')
    paginator = Paginator(reqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        formset = RequestForm(request.POST)
        if formset.is_valid():
            clean_form = formset.cleaned_data
            clean_form = formset.save(commit=False)
            clean_form.requested_by = request.user
            clean_form.save()
            return HttpResponseRedirect('/order/all')
    if request.method == 'GET':
        reqs = Requesition.objects.all()
        query = request.GET.get('control_number')
        if query:
            reqs = Requesition.objects.filter(Control_Number=query)
            paginator = Paginator(reqs, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    context = {'form':formset,'reqs':page_obj}
    return render(request,'main/create_order.html', context)

@login_required(login_url='/login/')
def pending(request):
    formset = RequestForm()
    reqs = Requesition.objects.filter(status = 'A').order_by('Date')
    paginator = Paginator(reqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        formset = RequestForm(request.POST)
        if formset.is_valid():
            clean_form = formset.cleaned_data
            clean_form = formset.save(commit=False)
            clean_form.requested_by = request.user
            clean_form.save()
            return HttpResponseRedirect('/order/all')
    if request.method == 'GET':
        reqs = Requesition.objects.all()
        query = request.GET.get('control_number')
        if query:
            reqs = Requesition.objects.filter(Control_Number=query)
            paginator = Paginator(reqs, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

    context = {'form':formset,'reqs':page_obj}
    return render(request,'main/create_order.html', context)

@login_required(login_url='/login/')
def accepted(request):
    formset = RequestForm()
    reqs = Requesition.objects.filter(status = 'B').order_by('Date')
    paginator = Paginator(reqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        formset = RequestForm(request.POST)
        if formset.is_valid():
            clean_form = formset.cleaned_data
            clean_form = formset.save(commit=False)
            clean_form.requested_by = request.user
            clean_form.save()
            return HttpResponseRedirect('/order/all')

    if request.method == 'GET':
        reqs = Requesition.objects.all()
        query = request.GET.get('control_number')
        if query:
            reqs = Requesition.objects.filter(Control_Number=query)
            paginator = Paginator(reqs, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

    context = {'form':formset,'reqs':page_obj}
    return render(request,'main/create_order.html', context)

@login_required(login_url='/login/')
def partial(request):
    formset = RequestForm()
    reqs = Requesition.objects.filter(status = 'C').order_by('Date')
    paginator = Paginator(reqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        formset = RequestForm(request.POST)
        if formset.is_valid():
            clean_form = formset.cleaned_data
            clean_form = formset.save(commit=False)
            clean_form.requested_by = request.user
            clean_form.save()
            return HttpResponseRedirect('/order/all')

    if request.method == 'GET':
        reqs = Requesition.objects.all()
        query = request.GET.get('control_number')
        if query:
            reqs = Requesition.objects.filter(Control_Number=query)
            paginator = Paginator(reqs, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)


    context = {'form':formset,'reqs':page_obj}
    return render(request,'main/create_order.html', context)

@login_required(login_url='/login/')
def delivered(request):
    formset = RequestForm()
    reqs = Requesition.objects.filter(status = 'D').order_by('Date')
    paginator = Paginator(reqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        formset = RequestForm(request.POST)
        if formset.is_valid():
            clean_form = formset.cleaned_data
            clean_form = formset.save(commit=False)
            clean_form.requested_by = request.user
            clean_form.save()
            return HttpResponseRedirect('/order/all')

    if request.method == 'GET':
        reqs = Requesition.objects.all()
        query = request.GET.get('control_number')
        if query:
            reqs = Requesition.objects.filter(Control_Number=query)
            paginator = Paginator(reqs, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    


    context = {'form':formset,'reqs':page_obj}
    return render(request,'main/create_order.html', context)

@login_required(login_url='/login/')
def details(request, id):
    req = Requesition.objects.get(id=id)
    mats = ReqToRaw.objects.filter(req=id)
    form = ReqToRawForm()
    if request.method == 'POST':
        form = ReqToRawForm(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            clean_form = form.save(commit=False)
            batch = RawBatch.objects.get(id=clean_form.raw.id)
            num = batch.quantity - clean_form.quantity_needed
            batch.quantity = num
            batch.save()
            clean_form.req = req
            clean_form.save()
            return HttpResponseRedirect('/order/details/'+id)

    context = {'req':req, 'form':form,'mats':mats}
    return render(request, 'main/details.html',context)

@login_required(login_url='/login/')
def revert(request,id):
    mat = ReqToRaw.objects.get(id=id)
    batch = RawBatch.objects.get(id=mat.raw.id)
    num = batch.quantity + mat.quantity_needed
    rev_id = mat.req.id
    batch.quantity = num
    batch.save()
    mat.delete()
    return HttpResponseRedirect('/order/details/'+str(rev_id))


@login_required(login_url='/login/')
def productView(request):
    form = ProductForm()
    prod = Product.objects.order_by('stock_quantity')
    paginator = Paginator(prod, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/product')
    context = {'prod_form':form, 'prods':page_obj}
    return render(request, 'main/product.html',context)

@login_required(login_url='/login/')
def customer(request):
    form = CustomerForm()
    customers = Customer.objects.all().order_by('name')
    paginator = Paginator(customers, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/customers')
    context = {'custs':page_obj,'form':form}
    return render(request, 'main/customer.html', context)

@login_required(login_url='/login/')
def customerDetail(request, id):
    customer = Customer.objects.get(id=id)
    pending = Requesition.objects.filter(customer_id=id,status='A')
    accepted = Requesition.objects.filter(customer_id=id,status='B')
    partial = Requesition.objects.filter(customer_id=id,status='C')
    delivered = Requesition.objects.filter(customer_id=id,status='D')
    context = {'cust':customer,'pends':pending,'acpts':accepted,'parts':partial,'delis':delivered}
    return render(request, 'main/customer_detail.html', context)

@login_required(login_url='/login/')
def acceptOrder(request,id):
    req = Requesition.objects.get(id=id)
    num = req.Item.stock_quantity - req.Qty
    item = Product.objects.get(id=req.Item.id)
    item.stock_quantity = num
    item.save()
    req.status = 'B'
    req.save()
    return HttpResponseRedirect('/order/details/'+id)

@login_required(login_url='/login/')
def updatePart(request,id):
    req = Requesition.objects.get(id=id)
    req.status = 'C'
    req.save()
    return HttpResponseRedirect('/order/details/'+id)

@login_required(login_url='/login/')
def updateFull(request,id):
    req = Requesition.objects.get(id=id)
    req.status = 'D'
    req.save()
    return HttpResponseRedirect('/order/details/'+id)

@login_required(login_url='/login/')
def raw(request):
    raws = RawMaterial.objects.all()
    context = {'raws':raws}
    return render(request, 'main/RawMaterials.html',context)

@login_required(login_url='/login/')
def rawDetails(request, id):
    raw = RawMaterial.objects.get(id=id)
    batches = RawBatch.objects.filter(tp=raw.id).order_by('date_created','-quantity')
    paginator = Paginator(batches, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'raw':raw,'batches':page_obj}
    return render(request, 'main/rawDetails.html',context)