from django.urls import path
from . import views

app_name="visualizer"

urlpatterns = [
    path('<int:voting_id>/', views.VisualizerView.as_view()),
    path('<int:voting_id>/esp', views.VisualizerView.as_view()),
    path('<int:voting_id>/eng', views.VisualizerViewENG.as_view()),
    path('<int:voting_id>/ale', views.VisualizerViewALE.as_view()),
]
