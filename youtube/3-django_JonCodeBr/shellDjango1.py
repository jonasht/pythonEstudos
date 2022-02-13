# coding: utf-8

from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username="admin")
user
user.email
user.username
user.id
user.password
user.is_authenticated
dir(user)
user.get_full_name
user.get_full_name()
post = Post(titulo='Testando o shell do django', slug='testando-o-shell,)
post = Post(titulo="Testando o shell do django", slug="testando-o-shell")
post = Post(
    titulo="Testando o shell do django",
    slug="testando-o-shell",
    conteudo="Testando o shell do django",
    autor=user,
)
post.save()
get_ipython().run_line_magic('py', 'manage.py runserver')
get_ipython().run_line_magic('python', 'manage.py runserver')
get_ipython().run_line_magic('!python', 'manage.py runserver')
post.titulo()
post.titulo
post.titulo = "testando o shell do django - atualizando os dados"
post.save()
post.titulo = "testando o shell do django - atualizando os dados1"
post.save()
def update_title(var):
    post.titulo = var
    post.save()
update_title("testando o shell do django")
