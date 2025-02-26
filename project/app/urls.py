from app.views import StudentViewSet,StaffViewSet,ParentsViewSet,EmployeeViewSet,TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Student', StudentViewSet, )
router.register(r'staff', StaffViewSet, )
router.register(r'parent', ParentsViewSet, )
router.register(r'emp', EmployeeViewSet, )
router.register(r'teacher', TeacherViewSet, )


urlpatterns = router.urls