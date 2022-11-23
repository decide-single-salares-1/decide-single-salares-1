from django.urls import path
from .views import BoothView, BoothViewESP, BoothViewALE


urlpatterns = [
    path('<int:voting_id>/', BoothView.as_view()),
    path('<int:voting_id>/esp', BoothViewESP.as_view()),
    path('<int:voting_id>/ale', BoothViewALE.as_view()),
]
