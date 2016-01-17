from rest_framework.routers import SimpleRouter

from . import views

api = SimpleRouter()
api.register(r'contributions', views.IndependentMoneyViewSet)
urlpatterns = api.urls
