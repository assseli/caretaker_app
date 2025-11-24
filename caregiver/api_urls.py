from rest_framework import routers
from .views import (
    UserViewSet, CaregiverViewSet, MemberViewSet, AddressViewSet,
    JobViewSet, JobApplicationViewSet, AppointmentViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'caregivers', CaregiverViewSet)
router.register(r'members', MemberViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'job-applications', JobApplicationViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls
