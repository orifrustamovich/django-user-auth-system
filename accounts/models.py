from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string
from datetime import timedelta
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading  # Asinxron holatni ta'minlash uchun

# CustomUser modeli
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

# Default expiry funksiyasi
def default_expiry():
    return now() + timedelta(minutes=1)

# Email tasdiqlash kodi modeli
class EmailConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    expiry = models.DateTimeField(default=default_expiry)

    def generate_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
        self.expiry = now() + timedelta(minutes=1)
        self.save()


# Asinxron vazifa: foydalanuvchini vaqtida tasdiqlamasa o'chirish
def delayed_delete(user, delay=60):
    """Tasdiqlanmagan foydalanuvchini belgilangan vaqt ichida o'chiradi."""
    def task():
        # Delay tugashini kutamiz
        threading.Event().wait(delay)
        # Tasdiqlanganligini tekshiramiz
        user.refresh_from_db()  # Yangilangan ma'lumotlarni olish
        if not user.email_confirmed:
            user.delete()

    thread = threading.Thread(target=task)
    thread.start()

# Signal: foydalanuvchi yaratilganda asinxron o'chirishni boshlash
@receiver(post_save, sender=CustomUser)
def handle_unconfirmed_user(sender, instance, created, **kwargs):
    if created and not instance.email_confirmed:
        delayed_delete(instance, delay=60)  # 1 daqiqa (60 sekund)
