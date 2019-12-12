from django.shortcuts import render
from .models import Post

class PostListView(generic.ListView):
	model = Post
	paginate_by = 10

class PostDetailView(generic.DetailView):
	model = Post

@login_required
def post_write(request):
	# save process
	if request.method == 'POST':
		form = CreatePostForm(request.POST)

		if form.is_valid():
			conn_user = request.user
			conn_user = request.conn_userconn_profile = Profile.objects.get(user=conn_user)
			nick = conn_profile.nick
			#new_post = Post()
			new_post = form.save(commit=False)
			new_post.writer = nick
			new_post.save()
			messages.info(request, 'Successfully Post!')
			return HttpResponseRedirect(reverse_lazy('board_index'))
	# send form
	else:
		form = CreatePostForm()

	return render(request, 'board/write_post.html', {'form': form})


