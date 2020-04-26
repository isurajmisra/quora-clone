from questans.models import UpVote
from django.contrib.auth.models import User 




# def upvote(user, answer):
#     if not user.is_upvoAnswerForm: AnswerForm
# ted(answer):
#         upvote = UpVote(user=user.id, answer=answer.id)
        

def downvote(user, answer):
    if user.is_upvoted(answer):
        UpVote.objects.filter(user_id=user.id, answer_id=answer.id).delete()


def is_upvoted(self,answer):
    if self.upvotes.filter(answer=answer).first():
       return True
    else:
        return False
        
  