from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .utils import send_confirmation_email
from .models import EmailConfirmationCode, CustomUser
from django.utils import timezone  # timezone import qilamiz

from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email_confirmed = False
            user.save()
            send_confirmation_email(user)
            request.session['user_id'] = user.id
            return redirect('confirm_email')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def confirm_email(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = CustomUser.objects.filter(id=user_id).first()
    if not user:
        return redirect('register')

    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            confirmation = EmailConfirmationCode.objects.get(user=user, code=code)
            # Naive va aware datetimelarni taqqoslashni oldini olish uchun timezone.now() ishlatamiz
            if confirmation.expiry > timezone.now():
                user.email_confirmed = True
                user.save()
                confirmation.delete()
                return redirect('login')
            else:
                user.delete()
                # request.session.flush()
                return redirect('register')
        except EmailConfirmationCode.DoesNotExist:
            return render(request, 'accounts/confirm_email.html', {'error': 'Invalid code'})
    return render(request, 'accounts/confirm_email.html')


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)  # ✅ Formga request kiritamiz

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()  # ✅ Foydalanuvchini olish

        if user.email_confirmed:  # ✅ Email tasdiqlanganligini tekshiramiz
            login(request, user)
            return redirect('home')  # ✅ Muvaffaqiyatli login
        else:
            form.add_error(None, "Emailingiz tasdiqlanmagan!")  # ✅ Form ichida xato ko‘rsatish

    return render(request, "accounts/login.html", {"form": form})  # ✅ Form va xatolarni yuborish



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.email_confirmed:  # Faqat tasdiqlangan emailga ruxsat beriladi
#                 login(request, user)
#                 return redirect('home')  # Foydalanuvchini uy sahifasiga yo'naltirish
#             else:
#                 return render(request, 'accounts/login.html', {'error': 'Email not confirmed'})
#         else:
#             return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'accounts/login.html')


