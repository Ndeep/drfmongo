from django_server_access_logs.models import AccesslogsModel
from django.conf import settings
from django.utils import timezone

class AccessLogsMiddleware(object):
    def __init__(self,get_response=None):
        self.get_response=get_response

    def __call__(self, request):
        if not request.session.session_key:
            request.session.create()

        access_log_data=dict()
        access_log_data['path']=request.path

        x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
        access_log_data['ip_address']=x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        access_log_data['method']=request.method
        access_log_data['referrer']=request.META.get('HTTP_REFERRER',None)
        access_log_data['session_key']=request.session.session_key

        data=dict()
        data['get']=dict(request.GET.copy())
        data['post']=dict(request.POST.copy())

        keys_to_remove=["password","csrfmiddlewaretoken"]
        for key in keys_to_remove:
            data['post'].pop(key,None)

        access_log_data['data']=data
        access_log_data['timestamp']=timezone.now()

        try:
            AccesslogsModel(**access_log_data).save()
        except Exception as e:
            pass

        response=self.get_response(request)
        return response