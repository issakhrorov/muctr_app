from django.urls import path
from .views import RoomView, signin, signup, export_to_excel

urlpatterns = [
    # path('', FormView.as_view(), name="form"),
    path("", signup, name="signup"),
    path("room/<str:pk>", RoomView.as_view(), name="room"),
    path("signin/", signin, name="signin"),
    path('export/', export_to_excel, name='export_to_excel'),
]