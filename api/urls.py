from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('users/', include('users.urls')),
    path('quotes/',include('quotes.urls')),
    path('trivia/',include('trivia.urls')),
    path('issuetracker/',include('issuetracker.urls')),
]
