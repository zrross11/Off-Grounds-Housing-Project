from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import ReviewForm
from .models import HousingOption, Review


class HousingListing(generic.ListView):
    template_name = "housing/listings.html"
    context_object_name = "housing_list"

    def get_queryset(self):
        return HousingOption.objects.filter()


class HousingMapping(generic.ListView):
    template_name = "housing/map.html"
    context_object_name = "housing_map"

    def get_queryset(self):
        return HousingOption.objects.filter()


class HousingInput(CreateView):
    template_name = "housing/form.html"
    model = HousingOption
    fields = ['name', 'address', 'numberOfBedrooms',
              'numberOfBathrooms', 'pricePerUnit', 'website', 'furnished', 'description', 'pic']
    success_url = '/housing'


class SearchView(generic.ListView):
    model = HousingOption
    template_name = 'housing/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            postresult = HousingOption.objects.filter(name__icontains=query)
            result = postresult
        else:
            result = None
        return result


def detailView(request, id):
    obj = HousingOption.objects.get(id=id)
    reviews = Review.objects.filter(housing=obj)

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.housing = obj
            review_form.instance.user = request.user
            review_form.save()
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    context = {
        "housing": obj,
        "reviews": reviews,
        "review_form": review_form
    }
    return render(request, "housing/details.html", context)


def dynamic_lookup_view(request, id):
    """
    Temporary Method for Detail Lookup
    """

    obj = HousingOption.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "housing/details.html", context)

def delete_housing_option(request, id):
    query = HousingOption.objects.get(id=id)
    query.delete()
    return redirect('../')
