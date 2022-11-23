from django.urls import path
from .views import BoothViewIng, BoothViewESP, BoothViewALE


urlpatterns = [
    path('<int:voting_id>/', BoothViewIng.as_view()),
    path('<int:voting_id>/ing', BoothViewIng.as_view()),
    path('<int:voting_id>/esp', BoothViewESP.as_view()),
    path('<int:voting_id>/ale', BoothViewALE.as_view()),
]
