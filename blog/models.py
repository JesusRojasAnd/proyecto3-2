from django.db import models
from django.contrib.auth.models import User # es el usuario de auth user
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,null=False, unique=True,verbose_name='Nombre')
    # tenemos un atributo nombre 
    # definimos un toString, self es el objeto this
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categorias' # nombre de la tabla de BD
        verbose_name =  'Categoria' # nombre en el panel de administración
        verbose_name_plural = 'Categorias'
        ordering =['id']  # ordenacion asc, con ['-id'] es desc
    

class Entrada(models.Model):
        autor = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        titulo =models.CharField(max_length=100, unique=True, null=False,blank=False,verbose_name='Título')
        contenido =models.TextField(null=True, verbose_name='Contenido')
        imagen = models.ImageField(upload_to='entradas/%Y/%m/%d',null=True,blank=True,verbose_name='Imagen')
        fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de alta')
        fecha_actualizacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualización')

        def __str__(self):
             return self.titulo
        
        class Meta:
            db_table = 'entradas' # nombre de la tabla de BD
            verbose_name =  'Entrada' # nombre en el panel de administración
            verbose_name_plural = 'Entradas'
            ordering =['id']  # ordenacion asc, con ['-id'] es desc