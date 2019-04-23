from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from assignment.forms import CreateAssignment , CreateQuestion
from assignment.models import Assignment , Question

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

class create_question(TemplateView):
    form_class = CreateQuestion
    template_name = 'teacher/create-question.html'
    model= Question

    def get(self,request):
        form = CreateQuestion()
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = CreateQuestion(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # text = form.cleaned_data['post']
            form = CreateQuestion()
            return redirect('assignment:create_question')
            
        args = {'form':form,'text':text}
        return render(request, self.template_name,args)

class asm_dashboard(TemplateView):
    template_name = 'teacher/assignment_dashboard.html'

    def get(self,request):
        asm_post = Assignment.objects.all()

        args = {'asm_post':asm_post}
        return render(request, self.template_name,args)
