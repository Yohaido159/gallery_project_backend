from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from .models import User
from .serializers import UserSerializer


from rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework import status
from rest_framework import generics

from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import requests

from gal_pro.settings import DOMIN


@api_view()
def django_rest_auth_null(a):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def django_rest_auth_prossess(request, key):
    to_post = {
        "key": f"{key}"
    }
    resp = requests.post(
        f'http://{DOMIN}/rest-auth/registration/verify-email/', data=to_post)

    return Response({"key": key, "msg": resp.json()}, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': _('Successfully confirmed email.')}, status=status.HTTP_200_OK)
        except EmailConfirmation.DoesNotExist:
            return Response({'detail': _('Error. Incorrect key.')}, status=status.HTTP_404_NOT_FOUND)

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise EmailConfirmation.DoesNotExist
        return emailconfirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs


# class UserApiPhone(generics.RetrieveAPIView):
#     model = User
#     serializer_class = UserSerializer
