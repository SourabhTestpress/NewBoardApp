python manage.py shell


>>> from boards.models import Board
>>> board1 = Board(name="Programming and Development",slug="",description="Related to Programming and Development only")
>>> board1.save()
>>> board1
<Board: Programming and Development>


>>> board1.slug
'programming-and-development'


>>> board1.description = "Limited to Programming and Development"
>>> board1.save()
>>> board1.description
'Limited to Programming and Development'


#Getting all the objects present in a Model
>>> board_list = Board.objects.all()
>>> for board in board_list:
...     print(board.description)
... 
It deals with Flora and Fauna
Limited to Programming and Development


#Getting a single object
>>> first = Board.objects.get(id=1)
>>> first.slug
'nature'
>>> Board.objects.get(name="Nature")
<Board: Nature>


#Experimenting with Topic
>>> from boards.models import Topic
>>> from django.contrib.auth.models import User
>>> me = User.objects.get(id=1)
>>> topic1 = Topic.objects.create(board=first,slug="",user=me,subject="Python")
>>> topic1
<Topic: Python>


# Experimenting with Relationship and Reverse relationship on shell
>>> topic1.board
<Board: Nature>
>>> first.topics.all()
<QuerySet [<Topic: Python>]>

