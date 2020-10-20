#from django.views.generic.base import TemplateView
from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
 									PageNotAnInteger
from django.views.generic import ListView
from myapp.models import Post, Comment
from django.core.mail import send_mail
from .forms import EmailPostForm ,CommentForm
from taggit.models import Tag
from django.db.models import Count

def post_list(request,tag_slug=None):
	object_list=Post.objects.all()
	#----tag-----
	tag=None
	if tag_slug: 
		tag=get_object_or_404(Tag, slug=tag_slug)
		object_list=object_list.filter(tags__in=[tag])
# -------- end tags-------
	paginator=Paginator(object_list,3) #her we want 2 objects(post) [pagination]
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		#if oage in not integer delivred the first page
		posts=paginator.page(1)
	except EmptyPage:
		#if page has out of range
		posts=paginator.page(paginator.num_pages)

	return render(request,'post_list.html',{'posts':posts,'page':page,'tag':tag})
#her we have details function
def post_details(request,year,month,day ,post):
	post=get_object_or_404(Post,slug=post,
								status='published',
								publish__year=year,
								publish__month=month,
								publish__day=day)
	#------- her we create comment system
	comments=post.comments.filter(active=True)
	new_comment=None
	if request.method=='POST':
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			#create comment objets but dont save it in database
			new_comment=comment_form.save(commit=False)
			new_comment.post=post
			#save the comment to the database
			new_comment.save()
			
	else:
		comment_form=CommentForm()
		#tags and similar tags
	post_tags_ids=post.tags.values_list('id',flat=True)
	similar_posts=Post.objects.filter(tags__in=post_tags_ids)
								
	similar_posts=similar_posts.annotate(same_tags=Count('tags'))\
								.order_by('-same_tags','-publish')[:4]


	return render(request,'post_details.html',{'post':post,
						'comments':comments,             # this context from comment=post.comment.filter with active comment 
						'comment_form':comment_form,     # this context from comment data form 
						'similar_posts':similar_posts})  # this context from similar post



#return pagination aith class based views
class PostListView(ListView):
	queryset=Post.objects.all()
	context_object_name='posts'
	paginate_by= 2
	template_name='post_list.html'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin22@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post': post,
                                      				'form': form,
                                                    'sent': sent})



