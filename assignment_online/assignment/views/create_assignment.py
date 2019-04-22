from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from assignment.forms import CreateAssignment
from assignment.models import Assignment

class create_assignment(TemplateView):
    form_class = CreateAssignment
    template_name = 'teacher/create-assignment.html'
    model= Assignment

    def get(self,request):
        form = CreateAssignment()
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = CreateAssignment(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # text = form.cleaned_data['post']
            form = CreateAssignment()
            return redirect('assignment:create_assignment')
            
        args = {'form':form,'text':text}
        return render(request, self.template_name,args)