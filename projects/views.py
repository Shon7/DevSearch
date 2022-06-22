
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import projectForm,ReviewForm
from .models import Project,Tag
from .utils import searchProjects,paginateProjects



def projects(request):
    projects,search_query = searchProjects(request)
    custom_range,projects = paginateProjects(request,projects,6)

    context = {'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)
def project(request,pk):
    projectObj = Project.objects.get(pid = pk)
    tags= projectObj.tags.all()
    form = ReviewForm()

    if request.method =='POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        return redirect('project',pk = projectObj.pid)

    context = {'project':projectObj,'tags':tags,'form':form}
    return render(request,'projects/single_project.html',context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(pid = pk)
    form = projectForm(instance=project)
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)
    
@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(pid = pk)
    context ={'object':project}
    if request.method == "POST":
        project.delete()
        return redirect('projects')

    return render(request,'delete_template.html',context)