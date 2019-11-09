from django.shortcuts import render, get_object_or_404, redirect
from .models import Market, Festival
from .forms import MarketForm
# Create your views here


def index(req):
    markets = Market.objects.all()
    festivals = Festival.objects.all()
    return render(req, 'index.html', {'markets': markets, 'festivals': festivals})


def market_detail(req, market_id):
    market_detail = get_object_or_404(Market, pk=market_id)
    return render(req, 'market_detail.html', {'market': market_detail})


def festival_detail(req, festival_id):
    festival_detail = get_object_or_404(Festival, pk=festival_id)
    return render(req, 'festival_detail.html', {'festival': festival_detail})


def market_new(req):
    if req.method == 'POST':
        marketform = MarketForm(req.POST)
        if marketform.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        marketform = MarketForm()
        return render(req, 'newMarket.html', {'marketform': marketform})
