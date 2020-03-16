from django.contrib.auth.backends import BaseBackend
from .models import User

class PhoneAuth(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(phone=username)
            if user.check_password(password):
                return user
            return None
        except:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None
            

