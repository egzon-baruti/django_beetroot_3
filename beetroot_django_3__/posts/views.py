# Importing the necessary modules
from django.views.generic import ListView
from .models import Post

# Creating a class-based view for the home page
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
