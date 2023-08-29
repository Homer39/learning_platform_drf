from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet
from materials.views.subject import SubjectCreateAPIView, SubjectListAPIView, SubjectUpdateAPIView, \
    SubjectDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('subject/', SubjectListAPIView.as_view(), name='subject_list'),
    path('subject/create/', SubjectCreateAPIView.as_view(), name='subject_create'),
    path('subject/update/<int:pk>/', SubjectUpdateAPIView.as_view(), name='subject_update'),
    path('subject/delete/<int:pk>/', SubjectDestroyAPIView.as_view(), name='subject_delete')
] + router.urls
