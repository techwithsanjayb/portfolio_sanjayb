from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def article_list(request):
    # Get all article categories for filtering options
    categories = article_category.objects.all()

    # Get the selected categories and search term from request GET parameters
    selected_categories = request.GET.getlist('category')  # List of selected categories
    search_term = request.GET.get('search', '')  # Search term (default to empty string if not provided)

    # Validate selected categories (only valid categories should be included)
    valid_category_ids = list(article_category.objects.values_list('id', flat=True))  # Get list of valid category IDs
    valid_selected_categories = []

    # Try to convert each selected category to an integer, and if it's valid, add it to the list
    for cat_id in selected_categories:
        try:
            if int(cat_id) in valid_category_ids:
                valid_selected_categories.append(cat_id)
        except ValueError:
            continue

    # Initialize the queryset with all articles
    article_data = article.objects.all()

    # Apply category filter if any valid categories are selected
    if valid_selected_categories:
        article_data = article_data.filter(article_category_belongs_to__id__in=valid_selected_categories)

    # Apply search term filter if a search term is provided
    if search_term:
        article_data = article_data.filter(
            Q(title__icontains=search_term) | Q(body__icontains=search_term)
        )

    # Order by creation date (assuming `created_at` is the field tracking article creation)
    article_data = article_data.order_by('-published_date')  # This orders the articles in descending order


    # Check if no articles match the filters
    if not article_data.exists():
        no_articles_found = True
    else:
        no_articles_found = False

    # Pagination
    paginator = Paginator(article_data, 6)  # 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass data to the template
    return render(request, 'core/article_list.html', {
        'article_obj': page_obj,
        'categories': categories,
        'selected_categories': valid_selected_categories,
        'search_term': search_term,
        'no_articles_found': no_articles_found  # Pass this flag to the template
    })


def article_detail(request, id):
     # Get all article categories for filtering options
    categories = article_category.objects.all()

    # Get the selected categories and search term from request GET parameters
    selected_categories = request.GET.getlist('category')  # List of selected categories
    search_term = request.GET.get('search', '')  # Search term (default to empty string if not provided)

    # Validate selected categories (only valid categories should be included)
    valid_category_ids = list(article_category.objects.values_list('id', flat=True))  # Get list of valid category IDs
    valid_selected_categories = []

    # Try to convert each selected category to an integer, and if it's valid, add it to the list
    for cat_id in selected_categories:
        try:
            if int(cat_id) in valid_category_ids:
                valid_selected_categories.append(cat_id)
        except ValueError:
            continue

    # Fetch the article with the given ID
    article_data = article.objects.get(id=id)

    return render(request, 'core/article_detail.html', 
        {'article_obj': article_data,'categories': categories,
        'selected_categories': valid_selected_categories,
        'search_term': search_term })  # Pass the article to the template



# class ArticleDetailView(DetailView):
#     model = article
#     template_name = 'core/article_detail.html'  # Make sure this template exists
#     context_object_name = 'article'


def resource_details(request):
    return render(request, 'core/resource_details.html')
    