from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import newReportForm
from .models import Report
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

@login_required
def consultas(request):
    if request.user.is_staff:
        consultas = Report.objects.all().order_by('-fechacreacion')
    else:
        consultas = Report.objects.filter(user=request.user).order_by('-fechacreacion')
    return render(request, 'consultas.html', {'data': consultas})

@login_required
def newreport(request):
    if request.method =="POST":
        form = newReportForm(request.POST, request.FILES)
        if form.is_valid():
            Report = form.save(commit=False)
            Report.user = request.user
            Report.save()
            return redirect('index')
    else:
        form = newReportForm()

    return render(request, 'nuevoreclamo.html', {'form': form})


@login_required
def detallereporte(request, id):
    # if request.user.is_staff():
    #     reporte = get_object_or_404(Report,id=id)
    # else:
    reporte = get_object_or_404(Report,id=id)
    if reporte.user == request.user or request.user.is_staff:
        return render(request, 'detallereclamo.html', {'reporte': reporte})
    else:
        raise PermissionDenied()
            
    
    
    