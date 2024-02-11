from django.shortcuts import render,redirect,HttpResponse
from .models import RegisterBook

# Create your views here.

def allbooks(req):
    bookdata = RegisterBook.objects.all()
    context = {"bookdata":bookdata}
    return render(req, "allbooks.html", context)

def registerbook(req):
    if req.method == "GET":
        return render(req,"registerbook.html")
    else:
        if (
            "photo" in req.FILES
            and "title" in req.POST
            and "author" in req.POST
            and "description" in req.POST
        ):
            photo = req.FILES["photo"]
            title = req.POST["title"]
            author = req.POST["author"]
            description = req.POST["description"]
            bookdata = RegisterBook.objects.create(title=title, author=author, description=description)
            bookdata.save()
            return redirect("/") 
        
def deletebooks(req,id):
    bookdata=RegisterBook.objects.filter(id=id)
    bookdata.delete()
    return redirect("/")

def editbooks(req,id):
    if req.method=="GET":
        bookdata=RegisterBook.objects.get(id=id)
        context={'bookdata':bookdata}
        return render(req,"editbooks.html",context)
    elif req.method=="POST":
        if ("photo" in req.FILES 
            and "title" in req.POST 
            and "author" in req.POST 
            and "description" in req.POST
        ):
    
            bookdata=RegisterBook.objects.get(id=id)
            bookdata.photo =req.FILES["photo"]
            bookdata.title =req.POST["title"]
            bookdata.author =req.POST["author"]
            bookdata.description =req.POST["description"]
            bookdata.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid request method")
            
