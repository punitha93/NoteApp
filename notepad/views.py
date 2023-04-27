from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Notes
from django.contrib.auth.models import User
from notepad.forms import SignupForm, NoteForm

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        note_form=NoteForm()
        return render(request, 'home.html', {'note_form':note_form})
    
def userdetails(request):       
    message = ""    
    signup_form = SignupForm()
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            message = "User successfully signed up"
        else:
            message  = "Plesae try Again"                 
        return redirect('/notes/login/', {'message':message})
    return render(request, 'user.html', context = {'signup_form':signup_form})
          

def login_user(request):
    message = ""       
    if request.method == 'POST':         
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)        
        if user is not None:
            login(request, user)                
            return redirect('/notes/notesave/')        
        else:            
            message = "Invalid username or password."  
    return render(request, 'login.html', {'message': message})


# def login_user(request):
#     message = ""       
#     if request.method == 'POST':        
#         login_form = LoginForm(data=request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data.get('username')
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)                
#                 return redirect('/notes/login/')        
#             else:            
#                 message = "Invalid username or password."                
#         else:
#             message = "Invalid form data. Please try again."
#     else:
#         login_form = LoginForm()
#     return render(request, 'login.html', {'login_form':login_form}, {'message': message})

def logout_view(request):
    if request=="POST":
        logout(request)
        return redirect('/notes/login/')
    return render(request,'home.html')

def notes(request):       
    if request.method =='GET':
        if not request.user.is_authenticated:
            return redirect('/notes/login/')                
        note = Notes.objects.filter(user=request.user.id)
        note_form = NoteForm()        
        return render(request, 'note_page.html', {'note':note, 'note_form':note_form})    
    if request.method =='POST':        
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note=note_form.save(commit=False)
            note.user=request.user
            note.save()            
            return redirect('/notes/notesave/')
            message="Saved!"
        else:
            message= "Something went wrong!"      
    return render(request, 'note_page.html', {'note':note, 'note_form':note_form, 'message':message})


def view_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    return render(request, 'viewnote.html', {'note':note})

def del_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    note.delete()
    return redirect('/notes/notesave/')