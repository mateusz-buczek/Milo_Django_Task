from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse

from .models import Profile
from .forms import UpdateProfileForm


class ProfileListView(ListView):  # main page view
    template_name = 'profile_list.html'
    model = Profile


class ProfileDetailView(DetailView):  # detailed user profile view
    template_name = 'custom_user/profile_details.html'
    model = Profile


# actually, this view is User create view, but thanks to signals it also creates linked profile
class CreateProfileView(CreateView):
    template_name = 'custom_user/create_profile.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('custom_user:update', args=(self.object.pk,))

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateProfileView(UpdateView):  # edit/update user's profile
    template_name = 'custom_user/update_profile.html'
    form_class = UpdateProfileForm
    model = Profile

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteProfileView(DeleteView):  # confirm/decline user deletion
    template_name = 'custom_user/delete_profile.html'
    model = User

    def get_success_url(self):
        return reverse('custom_user:profiles')


def csv_view(request):  # creates downloadable csv file mirroring content main page

    users = Profile.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    template = loader.get_template('custom_user/csv_template.txt')
    context = {
        'data': users,
    }

    response.write(template.render(context))
    return response
