from django.core.mail import send_mail
from .models import EmailConfirmationCode

def send_confirmation_email(user):
    code = EmailConfirmationCode.objects.create(user=user)
    code.generate_code()
    send_mail(
        'Email Confirmation Code',
        f'Your confirmation code is: {code.code}',
        'orifrustamovich71@gmail.com',
        [user.email],
        fail_silently=False,
    )