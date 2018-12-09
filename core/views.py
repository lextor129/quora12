from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect, redirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .models import User
from questans.models import Questions, Answers, QuestionGroups
from .forms import LoginForm, RegisterForm
from eggs.utils import render_alex

#generate pdf
from django.views import View
from django.template.loader import get_template
from eggs.myform import Myform
from eggs.models import Eggs
from eggs.utils import render_alex
from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
import random
from random import choice
#------------------

'''
class DashboardView(FormView):


    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Questions.objects.filter(user=user)
            content['userdetail'] = user
            content['questions'] = ques_obj
            ans_obj = Answers.objects.filter(question=ques_obj [0:1])
            content['answers'] = ans_obj
            return render(request, 'core/dashboard.html', content)
        else:
            return redirect(reverse('login-view'))

'''



'''class RegisterView(FormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'core/register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'core/register.html'
        return render(request, template, content)
'''


class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('MyView'))
        content['form'] = LoginForm
        return render(request, 'core/login.html', content)


    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username,password=password)
            login(request, user)
            return redirect(reverse('MyView'))
        except Exception:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'please insert correct credentials'
            return render_to_response('core/loginError.html', content)

class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/core/login')




#generate pdf

class GeneratePdf(View):


    def get(self, request, *args, **kwargs):
        if request.user.is_staff:

            raise Http404("No tienes permiso para generar pdf")
        if request.user.is_authenticated:
            #template = get_template('core/invoice.html')
            posts = Eggs.objects.all()
            count = Eggs.objects.count()
            print(request)

            type_a = Eggs.objects.filter(type='A').count()
            type_aa = Eggs.objects.filter(type='AA').count()
            type_extra= Eggs.objects.filter(type='EXTRA').count()
            type_b = Eggs.objects.filter(type='B').count()

            price =  Eggs.objects.aggregate(price_e=Sum('price'))
            pricee = price['price_e']
            quantity = Eggs.objects.aggregate(quantity_Y=Sum('quantity'))
            quantityy = quantity['quantity_Y']
           # price_p = Eggs.objects.values('id').annotate(exp=ExpressionWrapper(F('quantity') * F('price'),
                                                                      #output_field=FloatField()))
            #isinstance(Eggs.objects.none(), EmptyQuerySet)
            price_p = Eggs.objects.extra(select={
                'result': 'price*quantity', })



            total_price_p = Eggs.objects.aggregate(pq=Sum(F('quantity')*F('price')))

            pospri = zip(posts, price_p)


            context = {'posts': posts, 'count': count, 'price': price,
                       'type_aa': type_aa, 'type_extra': type_extra,
                       'type_b': type_b,   'quantity': quantity,
                       'type_a': type_a, 'pricee': pricee, 'quantityy': quantityy, 'price_p': price_p,
                       'total_price_p': total_price_p,'pospri':pospri
                       }


            pdf = render_alex.render_to_pdf('core/invoice_ht.html', context)


            #return render(request, 'core/invoice_ht.html', context)

            list_of_ints = list(range(3))

            def autoIncrement(a, b):
                x = range(a, b, 1)
                for i in x:
                     return str(i)


            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %choice(range(10000000000000)) #autoIncrement(1, 1000)#("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

        else:
            return redirect(reverse('login-view'))




#generate web
class GenerateHt(View):


    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            #template = get_template('core/invoice.html')
            posts = Eggs.objects.all()
            count = Eggs.objects.count()
            print(request)

            type_a = Eggs.objects.filter(type='A').count()
            type_aa = Eggs.objects.filter(type='AA').count()
            type_extra= Eggs.objects.filter(type='EXTRA').count()
            type_b = Eggs.objects.filter(type='B').count()

            price =  Eggs.objects.aggregate(price_e=Sum('price'))
            pricee = price['price_e']
            quantity = Eggs.objects.aggregate(quantity_Y=Sum('quantity'))
            quantityy = quantity['quantity_Y']
           # price_p = Eggs.objects.values('id').annotate(exp=ExpressionWrapper(F('quantity') * F('price'),
                                                                      #output_field=FloatField()))
            #isinstance(Eggs.objects.none(), EmptyQuerySet)
            price_p = Eggs.objects.extra(select={
                'result': 'price*quantity', })

            pospri = zip(posts, price_p)

            total_price_p = Eggs.objects.aggregate(pq=Sum(F('quantity')*F('price')))


            print(total_price_p)

            context = {'posts': posts, 'count': count, 'price': price,
                       'type_aa': type_aa, 'type_extra': type_extra,
                       'type_b': type_b,   'quantity': quantity,
                       'type_a': type_a, 'pricee': pricee, 'quantityy': quantityy, 'price_p': price_p,
                       'total_price_p': total_price_p,'pospri':pospri
                       }





            return render(request, 'core/invoice.html', context)



            '''if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")'''

        else:
            return redirect(reverse('login-view'))


#insert dates in db


class MyView(View):

    form_class = Myform
    initial = {'key': 'value'}
    template_name = 'core/form_template.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class
            return render(request, self.template_name, {'form': form})


        else:
            return redirect(reverse('login-view'))

    def post(self, request):
        form = self.form_class(request.POST)
        for formd in form:
             print(form)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            form.cleaned_data['customer']
            form = Myform
            return render(request, self.template_name, {'form': form, 'formd': formd})



        return render(request, self.template_name, {'form': form})


class PasteDetail(DetailView):
    model = Eggs
    template_name = "core/paste_detail.html"


#update date in database
class PasteUpdate(UpdateView):
    model = Eggs
    template_name = 'core/form_template.html'
    form_class = Myform
    print(form_class)
    queryset = Eggs.objects.all()
    success_url = reverse_lazy('table_eggs')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = self.form_class
            print(form)
            qu = self.queryset
            return render(self.request,self.template_name, {'form':form, 'qu':qu} )

        else:
            return redirect(reverse('login-view'))


    def get_object(self):
            id_ = self.kwargs.get("id")
            return get_object_or_404(Eggs, id=id_)


    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



