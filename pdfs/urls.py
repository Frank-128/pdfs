from django.urls import path
from .views import myHomePage,generate_pdf
urlpatterns = [
    path('first_page',myHomePage),
    path('generate_pdf',generate_pdf,name='generate_pdf')
]