import json

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.forms import ProjectRequestForm


class BadRequest(Exception):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class ProjectRequestCreate(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except:
            raise BadRequest('bad_json')

        form = ProjectRequestForm(data)
        if form.is_valid():
            project = form.save()
        else:
            return {
                'success': False,
                'errors': form.errors,
            }
        return {
            'success': True,
        }