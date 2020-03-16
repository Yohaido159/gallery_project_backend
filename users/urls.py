from django.urls import path, include, re_path
from rest_framework import routers
from .views import UserViewSet, django_rest_auth_null, VerifyEmailView, django_rest_auth_prossess

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [


    # all_auth
    path("accounts/", include("allauth.urls")),

    # rest_auth
    path('rest-auth/', include('rest_auth.urls')),

    re_path('rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
            django_rest_auth_prossess, name='account_email_verification_sent'),

    path('rest-auth/registration/verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/rest-auth/registration/account-email-verification-sent/',
         django_rest_auth_null, name='account_email_verification_sent'),

    path('rest-auth/password-reset/confirm/<str:uidb64>)/<str:token>/',
         django_rest_auth_null, name='password_reset_confirm'),
]

urlpatterns += router.urls
