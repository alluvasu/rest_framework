"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from a1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path ( 'api-auth/' , include ( 'rest_framework.urls' ) ),
    path ( 'sl/' ,views.Snippet_List  ) ,
    path ( 'csl/' , views.SnippetList.as_view() ) ,
    path ( 'sd/<pk>/' , views.snippet_detail ) ,
    path ( 'csd/<pk>/' , views.SnippetDetail.as_view() ) ,
    path ( 'csl1/', views.SnippetList.as_view() ) ,
    path ( 'ccsl1/', views.SnippetList.as_view() ) ,
    path ( 'csd1/<pk>/' , views.SnippetDetail.as_view ( ) ),
    path ( 'ccsd1/<pk>/' , views.SnippetDetail.as_view ( ) ),
    path ( 'ul1/' , views.UserList.as_view ( ) ) ,
    path ( 'ud/<pk>/' , views.UserDetail.as_view ( ) ) ,
    path ( 'api/' , views.api_view ( ) ) ,


    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),


]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from a1 import views


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])
from a1.views import api_root ,UserViewSet,SnippetViewSet
## viewsets setting up url patterens

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
### view set explicitly url patterens

urlpatterns = format_suffix_patterns([
    path ( 'users/' , user_list , name='user-list' ) ,
    path ( 'snippet/' , snippet_list , name='snippet-list' ) ,
    path ( 'snippet/<pk>' , snippet_detail , name='snippet-detail' ) ,

    path ( 'users/<pk>/' , user_detail , name='user-detail' ) ,
    ])

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]