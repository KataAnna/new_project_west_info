from django.urls import path, include
from market.views.auth import AuthView, hello

from market.views.company import CompanyListView

urlpatterns = [
    path('userlogin/', AuthView.as_view()),
    path('hello', hello),
    path('company_list', CompanyListView.as_view()),
]