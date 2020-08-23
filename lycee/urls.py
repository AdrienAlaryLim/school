from django.conf.urls import url
from . import views
from .views import StudentCreateView, ParticularPresenceCreateView
from .views import EditStudentView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
		url(r'^student/(?P<pk>\d+)/edit/$', EditStudentView.as_view(), name='edit_student'),
		url(r'^cursuscall/(?P<cursus_id>[0-9]+)$', views.cursusCallOf, name='cursus_call'),
		url(r'^cursuscall/send/$', views.cursusCallOfTreatment, name='cursus_call_treat'),
		url(r'^call/$', ParticularPresenceCreateView.as_view(), name='create_presence'),
		url(r'^call/details$', views.DetailPresence, name='details_presence')
]
