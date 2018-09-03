from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_api_demo.views import AuthorViewSet,BookViewSet,ToolViewSet

router=routers.DefaultRouter()
router.register(r'tool', ToolViewSet, r"tool")
router.register(r'author', AuthorViewSet, r"author")
router.register(r'book', BookViewSet, r"book")

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
]
