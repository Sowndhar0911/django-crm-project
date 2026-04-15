from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from .forms import LeadForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Count


@login_required
def dashboard(request):
    total_leads = Lead.objects.count()
    new_leads = Lead.objects.filter(status='NEW').count()
    closed_won = Lead.objects.filter(status='WON').count()
    closed_lost = Lead.objects.filter(status='LOST').count()

    return render(request, 'leads/dashboard.html', {
        'total_leads': total_leads,
        'new_leads': new_leads,
        'closed_won': closed_won,
        'closed_lost': closed_lost,
    })




def lead_list(request):
    search = request.GET.get('search', '')

    leads = Lead.objects.filter(
        Q(name__icontains=search) |
        Q(phone__icontains=search) |
        Q(product_category__icontains=search) |
        Q(product_model__icontains=search)
    )

    paginator = Paginator(leads, 5) 
    page_number = request.GET.get('page')
    leads = paginator.get_page(page_number)

    return render(request, 'leads/lead_list.html', {
        'leads': leads,
        'search': search
    })



def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
        else:
            print(form.errors)
    else:
        form = LeadForm()
    return render(request, 'leads/lead_add.html', {'form': form})


def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads/lead_update.html', {'form': form})


def delete_lead(request, pk):
    lead = get_object_or_404(Lead, id=pk)

    if request.method == "POST":
        lead.delete()
        return redirect('lead_list')

    return render(request, 'leads/lead_confirm_delete.html', {'lead': lead})

