from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as lazy

from app import views

app_name = 'contributors'
urlpatterns = [
    path('', views.home.HomeView.as_view(), name='home'),
    path(
        'registration',
        views.registration.RegistrationView.as_view(),
        name='registration',
    ),
    path(
        'organizations',
        views.organizations.ListView.as_view(),
        name='organizations_list',
    ),
    path(
        'organizations/<int:pk>',
        views.organization.DetailView.as_view(),
        name='organization_details',
    ),
    path(
        'repositories',
        views.repositories.ListView.as_view(),
        name='repositories_list',
    ),
    path(
        'repositories/<int:pk>',
        views.repository.DetailView.as_view(),
        name='repository_details',
    ),
    path(
        'contributors',
        views.contributors.ListView.as_view(),
        name='contributors_list',
    ),
    path(
        'contributors/<int:pk>',
        views.contributor.DetailView.as_view(),
        name='contributor_details',
    ),
    path('event-handler', views.webhook.EventHandler.as_view()),
]

admin.site.index_title = lazy('Hexlet Friends')
admin.site.site_header = lazy('Site administration')
admin.site.site_title = lazy('Site Administration')
