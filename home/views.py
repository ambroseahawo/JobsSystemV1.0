from django.shortcuts import render, redirect
from django.views.generic import View
from jobs.models import Job
from django.core.paginator import Paginator, EmptyPage


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        """ get request for home page"""

        paginator = Paginator(Job.objects.all().order_by('id'), 6)
        context = {}

        page = request.GET.get('page', 1)

        try:
            jobs = paginator.page(page)

            context = {
                'jobs': jobs,
            }
        except EmptyPage:
            pass

        return render(request, self.template_name, context)

    def post(self, request):
        """Picks up search request and forwards it to the search view"""

        search = request.POST['search']
        search_param = request.POST['search_param']

        if not search:
            return redirect('home:index')

        return redirect('jobs:search_job', search_param, search)
