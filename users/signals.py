# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from users.models import CustomUser
#
#
# @receiver(post_save, sender=CustomUser)
# def send_welcome_email(sender, instance, created, **kwargs):
#     print("Created", created)
#     if created:
#         send_mail(
#             "Goodreadsga xush kelibsiz!",
#             f"Salom {instance.username}. Goodreadsga xush kelibsiz!. Kitoblar va sharxlardan rohatlaning.",
#             'shohijahonyodgorov2141@gmail.com',
#             [instance.email]
#         )
#
