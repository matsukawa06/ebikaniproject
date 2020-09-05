from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm
from django.views import generic
from django.urls import reverse_lazy

class ReviewList(generic.ListView):
    model = Review

class ReviewDetail(generic.DetailView):
    model = Review

class ReviewCreate(generic.CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')

class ReviewUpdate(generic.UpdateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')

class ReviewDelete(generic.DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')

# get_object_or_404 を使用しない場合の書き方
""" 
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        raise Http404
    
    context = {
        'review': review,
    }
    return render(request, 'reviews/review_detail.html', context)
 """
