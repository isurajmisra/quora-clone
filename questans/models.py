from django.db import models
from django.conf import settings
from django.utils.text import slugify
from core.models import User
from taggit.managers import TaggableManager



class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='questions')
    title = models.TextField()
    topics = TaggableManager(related_name='topics')
    created_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)



class UpVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='upvotes')
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE,related_name='upvotes')

    # def upvote(self, answer):
    #     if not self.is_upvoted(answer):
    #         upvote = UpVote(user=self.id, answer=answer.id)
    #         upvote.save()
        

    # def downvote(self, answer):
    #     if self.is_upvoted(answer):
    #         UpVote.objects.get(user=self.id, answer=answer.id).delete()

    # def is_upvoted(self, answer, user):
    #     return (
    #         UpVote.objects.filter(
    #             UpVote.user.id == user.id, UpVote.answer.id == answer.id
    #         ).count()
    #         > 0
    #     )
    