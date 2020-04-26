from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    def is_upvoted(self,pk):
        answer = get_object_or_404(Answers,pk=pk)
        if self.upvotes.filter(answer=answer)==answer.upvotes.filter(user=self):
            return True
        else:
            return False


    


