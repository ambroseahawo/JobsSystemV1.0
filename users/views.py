import os
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .models import Account, Experience, Industry, Education, Skill, Media, Job
from .forms import CompleteProfileForm, ExperienceForm, InterestsForm, EducationForm, SkillForm
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse


class AccountView(View):
    template_name = 'account.html'
    form_class = [CompleteProfileForm, ExperienceForm, InterestsForm, EducationForm, SkillForm]

    def get(self, request):
        form = self.form_class[0](None)
        form2 = self.form_class[1](None)
        form3 = self.form_class[2](None)
        form4 = self.form_class[3](None)
        form5 = self.form_class[4](None)

        countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Capo Verde', 'Cameroon',
                     'Central African Republic', 'Chad', 'Comoros', 'DRC Congo', 'Republic of the Congo',
                     "Cote d'Ivoire", 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea',
                     'Eswatini(formely Swaziland)', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau',
                     'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
                     'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Rwanda', 'Sao Tome and Principe', 'Senegal',
                     'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania',
                     'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbambwe'
                     ]

        context = {
            'form': form,
            'experience_form': form2,
            'interests_form': form3,
            'education_form': form4,
            'skills_form': form5,
            'countries': countries
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.FILES:
            dp = request.FILES['user_dp']
            request.user.account.dp = dp or request.user.account.dp
        else:
            headline = request.POST['headline']
            country = request.POST['country']
            summary = request.POST['summary']
            hobbies = request.POST['hobbies']

            request.user.account.headline = headline or request.user.account.headline
            request.user.account.country = country or request.user.account.country
            request.user.account.summary = summary or request.user.account.summary
            request.user.account.hobbies = hobbies or request.user.account.hobbies

        request.user.account.save()

        return redirect('users:account')


class SignUpView(View):

    def get(self, request):
        context = {}

        return render(request, context)

    def post(self, request):
        """Picks up filled sign up form
           Authenticates the signed up user
           Creates Account object for user object
           logs in signed up user
           """

        if request.POST['password'] == request.POST['confirm-password']:
            username = request.POST['username']
            email = request.POST['email']
            password = make_password(request.POST['password'])

            user = User(
                username=username,
                email=email,
                password=password
            )
            user.save()

            Account.objects.create(
                user=user,
            )

            if user.is_active:
                login(request, user)

                return redirect('users:account')
        else:
            return redirect('users:login')


class LoginView(View):
    template_name = 'signup.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)

    def post(self, request):
        """logs in user"""

        username = request.POST['username']
        try:
            user = User.objects.get(username=username)
            pwd_valid = check_password(request.POST['password'], user.password)

            if pwd_valid:
                if user.is_active:
                    login(request, user)

                    if user.is_superuser:
                        return redirect('/admin')

                    return redirect('users:account')
            else:
                return redirect('users:login')

        except User.DoesNotExist:
            return redirect('users:login')


class LogoutView(View):

    def get(self, request):
        """Logs out logged in user"""

        logout(request)

        return redirect('home:index')


class AddExperienceView(View):

    def post(self, request):

        Experience.objects.create(
            user=request.user,
            position=request.POST['position'],
            role=request.POST['role']
        )

        content = {}

        return JsonResponse(data=content)


class AddInterestView(View):
    form_class = InterestsForm

    def post(self, request):
        form = self.form_class(request.POST)
        content = {}

        if form.is_valid():
            for interest in form.cleaned_data['interests']:
                request.user.account.interests.add(interest)

        return JsonResponse(content)


class AddEducationView(View):
    form_class = EducationForm

    def post(self, request):

        Education.objects.create(
            user=request.user,
            school=request.POST['school'],
            degree=request.POST['degree'],
            grade=request.POST['grade'],
            activities=request.POST['activities']
        )

        content = {}

        return JsonResponse(content)


class AddSkillView(View):

    def post(self, request):

        Skill.objects.create(
            user=request.user,
            title=request.POST['title'],
            about=request.POST['about']
        )

        content = {}

        return JsonResponse(content)


class DeleteExperienceView(View):

    def get(self, request, **kwargs):
        experience = Experience.objects.get(id=kwargs['pk'])
        experience.delete()
        content = {}

        return JsonResponse(content)


class DeleteInterestView(View):

    def get(self, request, **kwargs):
        interest = Industry.objects.get(id=kwargs['pk'])
        request.user.account.interests.remove(interest)
        request.user.account.save()

        content = {}

        return JsonResponse(content)


class DeleteEducationView(View):

    def get(self, request, **kwargs):
        education = Education.objects.get(id=kwargs['pk'])
        education.delete()
        content = {}

        return JsonResponse(content)


class DeleteSkillView(View):

    def get(self, request, **kwargs):
        skill = Skill.objects.get(id=kwargs['pk'])
        skill.delete()
        content = {}

        return JsonResponse(content)


class CompleteProfileView(View):

    def post(self, request):
        user = request.user

        user.account.address_line_1 = request.POST['addressLine1']
        user.account.address_line_2 = request.POST['addressLine2']
        user.account.city = request.POST['city']
        user.account.state = request.POST['state']
        user.account.postal_code = request.POST['postcode']
        user.email = request.POST['email']
        user.account.phone_number = request.POST['phoneNumber']

        user.save()
        user.account.save()

        return redirect('users:account')


class UploadDocumentsView(View):

    def post(self, request):

        if request.FILES:
            media = Media(
                user=request.user,
                file=request.FILES['document']
            )
            media.save()

        return redirect('users:account')


class OpenMediaView(View):

    def get(self, request, **kwargs):
        media = Media.objects.get(id=kwargs['pk'])

        path = media.file.path

        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response


class DeleteMediaView(View):

    def get(self, request, **kwargs):
        media = Media.objects.get(id=kwargs['pk'])
        media.delete()

        return redirect('users:account')


class RemoveShortlistedJobView(View):

    def get(self, request, **kwargs):
        job = Job.objects.get(id=kwargs['pk'])
        request.user.account.jobs.remove(job)

        return redirect('users:account')
