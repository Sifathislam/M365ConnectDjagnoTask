from django.shortcuts import render
from .models import Jobs
#============== Import the pagination packages =============#
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



#=============== Paginator main funtion ===============#
def pagination(request):
    job_List = Jobs.objects.all()
    paginator = Paginator(job_List, 3) #Show  3 Job in a per single page 

    page = request.GET.get('page')
    try: 
        job_List = paginator.page(page)

    #======== If the page is not a integer Show the first page ========#
    except PageNotAnInteger:
        job_List = paginator.page(1)

    #======== If  page is out of range =======#
    except EmptyPage:
        job_List = paginator.page(paginator.num_pages)

    #===== Render the page ====#
    return render(request, 'jobs.html',{'job_list': job_List})
    



