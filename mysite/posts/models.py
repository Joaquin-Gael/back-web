from django.db import models
from users.models import User

#Create Validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import os

def validate_file_extencion(value) -> None:
    valid_extencion = ['.png', '.jpg', '.jpeg','.pdf','.docx','.pptx','.pptm','.potx','.docm','.dotx','.dotm','.sql']
    try:
        ext = os.path.splitext(value.name)[1]
        if ext not in valid_extencion:
            raise ValidationError('Extencion no valida')
    except:
        raise ValidationError('Extencion no valida')
        


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def amount_likes(self) -> int:
        """RETORNA LA CANTIDAD DE LIKES QUE ESTEN RELACIONADOS CON EL POST"""
        return Like.objects.filter(post=self).count()
    
    def get_file_post(self) -> object | None:
        """RETORNA LA DATA DE EL ARCHIVO RELACIONADO CON EL POST"""
        return FilePost.objects.filter(post=self).first()

    def __str__(self) -> str:
        return f'''
            {self.title},
            {self.text},
            {self.created_at},
            {self.updated_at}
        '''
    
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'''
            {self.post},
            {self.text},
            {self.created_at}
        '''
    
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']
    
    def __unicode__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'''
            {self.post},
            {self.user}
        '''
    
    class Meta:
        db_table = 'likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['id']
    
    def __unicode__(self):
        return self.user

class FilePost(models.Model):
    name_file = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/',validators=[validate_file_extencion])