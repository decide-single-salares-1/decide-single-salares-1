from django.urls import path
from .views import VisualizerView, VisualizerViewENG, VisualizerViewALE


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('<int:voting_id>/esp', VisualizerView.as_view()),
    path('<int:voting_id>/eng', VisualizerViewENG.as_view()),
    path('<int:voting_id>/ale', VisualizerViewALE.as_view()),
]
