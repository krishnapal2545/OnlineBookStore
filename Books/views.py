from typing import List
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
import string , random , math
from .lists import *

def home(request):
    login=False
    if 'admin' in request.session:
        login=True
    author = set()
    genre = set()
    lang = set()
    name = set()
    bookid = set()
    books = Book.objects.all()
    for book in books:
        author.add(book.author)
        genre.add(book.genre)
        lang.add(book.language)
        bookid.add(book.bookid)
        name.add(book.name)
    
    param={'login':login,'auth':len(author),'gen':len(genre),'lang':len(lang),'book':len(bookid),'title':len(name)}
    return render(request,'home.html',param)

def login(request):
    if request.method == 'POST':
        logid=request.POST['logid']
        passw=request.POST['pass']
        if Admin.objects.filter(logid=logid,password=passw).exists():
            admin = Admin.objects.filter(logid=logid,password=passw).first()
            request.session['admin']=admin.adminid
            return redirect('/')
    return render(request,'login.html')

def logout(request):
    if 'admin' in request.session:
        del request.session['admin']
    return redirect('/')

def addbook(request):
    if request.session['admin']:
        if request.method=='POST':
            name=request.POST['name']
            auth=request.POST['auth']
            genre=request.POST['genre']
            lang=request.POST['lang']
            photo = request.POST['photo']
            if Book.objects.filter(name=name,author=auth,genre=genre,language=lang).exists():
                Result="Book is alredy exist"
                messages.warning(request,Result)
            else:
                while True :
                    id=''.join(random.choices(string.ascii_uppercase + string.digits,k=9))
                    if Book.objects.filter(bookid=id).exists() :
                        continue
                    else :
                        break
                create= Book.objects.create(bookid=id,name=name,author=auth,genre=genre,language=lang,photo=photo,adminid=request.session['admin'])
                create.save();
                Result="Book Saved Successfully!!"
                messages.success(request,Result)
        param = {'login':True,'Genre':Genre,'Lang':Language}
        return render(request,'addbook.html',param)
    return redirect('/')

def booklist(request):
    login=False
    post=6
    author = {'All'}
    genre = {'All'}
    lang = {'All'}
    bookid = {'All'}
    boo,aut,lan,gen='All','All','All','All' 
    bookids=[]
    bookgens=[]
    booklans=[]
    bookauts =[]
    if 'admin' in request.session:
        login=True
    books = Book.objects.all()
    last = math.ceil( len(books)/post)
    page = request.GET.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    books= books[(page-1) * post : (page-1) * post + post ]
    if page == 1:
        prev = "#"
        old = "/books/?page="+ str(page+1)
    elif page == last :
        prev = "/books/?page="+ str(page-1)
        old = "#"
    else:
        prev = "/books/?page="+ str(page-1)
        old = "/books/?page="+ str(page+1) 
    for book in books:
        author.add(book.author)
        genre.add(book.genre)
        lang.add(book.language)
        bookid.add(book.bookid)
    param={'login':login,'Books':books,'Authors':author,
    'Genres':genre,'Languages':lang,'Bookids':bookid,
    'boo':boo,'gen':gen,'lan':lan,'aut':aut,
    'prev':prev,'old':old,'num':page,'last':last,'page':True
    }
    if request.method == 'POST':
        boo = request.POST['bookid']
        gen = request.POST['genre']
        lan = request.POST['lang']
        aut = request.POST['auth']
        if boo != 'All': bookids = list(Book.objects.filter(bookid=boo).all())
        if gen != 'All': bookgens = list(Book.objects.filter(genre=gen).all())
        if lan != 'All': booklans = list(Book.objects.filter(language=lan).all())
        if aut != 'All': bookauts = list(Book.objects.filter(author=aut).all())
        books = bookids + bookauts + bookgens + booklans
        if boo == 'All' and gen == 'All' and lan == 'All' and aut == 'All' :
            return redirect('/books')

        param={'login':login,'Books':books,'Authors':author,
        'Genres':genre,'Languages':lang,'Bookids':bookid,
        'boo':boo,'gen':gen,'lan':lan,'aut':aut,
        }
    return render(request,'booklist.html',param)