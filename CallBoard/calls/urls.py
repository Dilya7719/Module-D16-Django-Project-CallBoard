from django.urls import path
from .views import CallsList, CallCreate, CallUpdate, CallDelete, MyCallsList, RespondSend, MyRespondList,\
   respond_accept_yes, respond_accept_no


urlpatterns = [
   path('', CallsList.as_view(), name='call_list'),
   path('my/', MyCallsList.as_view(), name='my_call_list'),
   path('<int:pk>', RespondSend.as_view(), name='respond_send'),
   path('accept/<int:pk>/', respond_accept_yes, name='respond_accept_yes'),
   path('reject/<int:pk>/', respond_accept_no, name='respond_accept_no'),
   path('create/', CallCreate.as_view(), name='call_create'),
   path('<int:pk>/edit/', CallUpdate.as_view(), name='call_edit'),
   path('<int:pk>/delete/', CallDelete.as_view(), name='call_delete'),
   path('my/responds/', MyRespondList.as_view(), name='my_respond_list'),
]