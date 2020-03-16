from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_FRONT + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
