"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

# from django.contrib import admin # não presente originalmente, mas presente no arquivo do porfessor
# from django.urls import path     # não presente originalmente, mas presente no arquivo do porfessor
from core import views             # importa módulo "views" da pasta "core"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/<nome>/<int:idade>', views.hello), # cria rota 'hello/' que aponta método "hello" no arquivo "views" da pasta "core"
#           |            |    |
#           |            |    +--> segundo parâmetro
#           |            +--> força segundo parâmetro como inteiro (página da erro se for outro tipo)
#           +--> segundo parâmetro

    path('add/<int:n1>/<int:n2>', views.add), # cria rota 'add/' que aponta método "add" no arquivo "views" da pasta "core"
    path('sub/<int:n1>/<int:n2>', views.sub), # cria rota 'sub/' que aponta método "add" no arquivo "views" da pasta "core"
    path('mul/<int:n1>/<int:n2>', views.mul), # cria rota 'mul/' que aponta método "add" no arquivo "views" da pasta "core"
    path('div/<int:n1>/<int:n2>', views.div)  # cria rota 'div/' que aponta método "add" no arquivo "views" da pasta "core"
]
