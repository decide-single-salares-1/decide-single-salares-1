from django.urls import path
from . import views

app_name="visualizer"

urlpatterns = [
    path('<int:voting_id>/', views.VisualizerView.as_view()),
]
