from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Job
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import User
from django.http.response import JsonResponse


class RecommendationsView(View):
    template_name = 'index.html'

    def get(self, request):
        """ get request for home page"""

        industries = [industry for industry in request.user.account.interests.all()]

        found = set()
        unique = [job for job in Job.objects.filter(industries__in=industries) if job not in found and not found.add(job)]
        paginator = Paginator(unique, 6)
        context = {}

        page = request.GET.get('page', 1)

        try:
            jobs = paginator.page(page)

            context = {
                'jobs': jobs,
                'current_page': 'Recommendations'
            }
        except EmptyPage:
            pass

        return render(request, self.template_name, context)

    def post(self, request):
        search_param = request.POST['search_param']
        search = request.POST['search']

        return redirect('jobs:search_job', search_param, search)


class JobSearchView(View):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        """Filters data from database returns it to satisfy search query"""

        context = {
            'value': kwargs['value'],
        }

        if kwargs['param'] == 'jobs' or kwargs['param'] == 'all':
            jobs = [job for job in Job.objects.filter(Q(position__contains=kwargs['value']) |
                                                      Q(company__contains=kwargs['value']))]
            context['jobs'] = jobs
            context['current_page'] = 'Searched for Jobs'

        elif kwargs['param'] == 'people':
            people = [user for user in User.objects.filter(username__icontains=kwargs['value'])]

            context['people'] = people
            context['current_page'] = 'Searched for People'

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        """Picks up search request and forwards it to the search view"""

        search = request.POST['search']
        search_param = request.POST['search_param']
        if not search:
            return redirect('home:index')

        return redirect('jobs:search_job', search_param, search)


class ShortlistJobView(View):
    def get(self, request, **kwargs):
        job = Job.objects.get(id=kwargs['pk'])

        content = {}

        if job not in request.user.account.jobs.all():
            request.user.account.jobs.add(job)
            content['message'] = 'shortlisted'
        else:
            request.user.account.jobs.remove(job)
            content['message'] = 'job removed from shortlisted'

        return JsonResponse(content)




