from django.conf.urls import url
from  rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import AuthRegister,AuthLogin

urlpatterns=[
    url(r'^login/',obtain_jwt_token),
    url(r'^token-refresh/',refresh_jwt_token),
    url(r'^token-verify',verify_jwt_token),
    url(r'^register/$',AuthRegister.as_view()),
    url(r'^logiin/$',AuthLogin.as_view()),
]