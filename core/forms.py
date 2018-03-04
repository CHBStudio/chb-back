from datetime import datetime

from django.forms import Form, CharField, EmailField, forms

from core.models import ProjectRequest


class ProjectRequestForm(Form):
    name = CharField(max_length=255)
    contact = CharField(max_length=255, required=True)

    def save(self):
        project_request = ProjectRequest()

        project_request.name = self.cleaned_data['name']
        contact = self.cleaned_data['contact']
        if '@' in list(contact):
            project_request.email = contact
        else:
            project_request.email = contact

        project_request.created_at = datetime.now()
        project_request.save()

        return project_request
