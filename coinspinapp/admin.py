from django.contrib import admin
from .models import *
# from firebase_admin import firestore
from firebase_admin import firestore
# Register your models here.

class FirestoreModel(admin.ModelAdmin):
        list_display = ('Title', 'Detail','Link')
        db = firestore.client()
        
        def get_queryset(self, request):
                db = firestore.client()
                post_ref = db.collection(u'Post')
                docs = post_ref.stream()
                # print(docs)
                posts = []
                for doc in docs:
                        print(f'{doc.id}')
                        data = doc.to_dict()
                        post = Post.objects.update_or_create(
                                    sno=doc.id,
                                    Title=data['Title'],
                                    Detail=data['Detail'],
                                    Link=data['Link']
                                )
                        posts.append(post)
        
                return Post.objects.all()
                #         post = Post(id=doc.id, Title=data['Title'], Detail=data['Detail'], Link=data['Link'])
                #         posts.append(post)
                # return posts
admin.site.register(Post,FirestoreModel)
