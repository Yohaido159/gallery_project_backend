# import os

# from django.http import StreamingHttpResponse

# from rest_framework.decorators import api_view
# import requests


# # @api_view()
# # def download(request):
# #     print("strt")
# #     url_image = request.GET.get("url")
# #     filename = os.path.basename(url_image)
# #     r = requests.get(url_image, stream=True)
# #     response = StreamingHttpResponse(streaming_content=r)
# #     response['Content-Disposition'] = f'attachement; filename="{filename}"'
# #     return response
