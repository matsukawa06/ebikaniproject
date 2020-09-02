from django.shortcuts import render
from .models import Review

def review_list(request):
    context = {
        'review_list': Review.objects.all(),
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {
        'review': review,
    }
    return render(request, 'reviews/review_detail.html', context)