from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.AddIssueView.as_view(), name='add_issue'),
	path('view', views.GetIssueView.as_view(), name='add_issue'),
	path('update/<int:number>', views.UpdateIssueView.as_view(), name='update_issue'),
]