from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        db_table = 'usuarios'


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='grupos')
    numero_miembros = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='grupos')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'grupos'


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='comentarios')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.comentario[:30]}..."  

    class Meta:
        db_table = 'comentarios'


class GrupoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='grupo_usuario')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='grupo_usuario')

    def __str__(self):
        return f"Grupo: {self.grupo.nombre}, Usuario: {self.usuario.nombre}"

    class Meta:
        db_table = 'grupo_usuario'
