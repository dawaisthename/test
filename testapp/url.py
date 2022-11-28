from django.urls import path
from . import views as view
urlpatterns = [
    path('',view.test_all,name='all'),
    path('insert/',view.test_insert,name='insert'),
    path('remove/<int:id>',view.test_remove,name='remove'),
    path('edit/<int:id>',view.test_update,name='edit'),



]