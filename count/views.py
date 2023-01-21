from django.shortcuts import redirect, render
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import word_count

# Create your views here.      
def home(request):
    content=word_count.objects.all()
    if request.method=='POST':
        try:
            #post link from user input
            link=request.POST['link']
            #get the link details
            res = requests.get(link)
            #convert response content to html
            soup = BeautifulSoup(res.content, 'html.parser')
            string=soup.text
            #find word count
            length=len(string.split())
            all_links = []
            media_link=[]
            #grab all a and img tags from the html
            links = soup.select('a')
            media=soup.select('img')

            #append datas to the array
            for href in links:
                text = href.get('href')
                if 'http' or '.com' in text:
                    all_links.append(text)
            for i in media:
                src=i.get('src')
                media_link.append(src)
        #save details to db
            word_count(currentLink=link,wordCount=length,links=all_links,mediaLinks=media_link).save()
           

            return redirect('home')
        except:
            messages.error(request, 'please enter invalid link')
            return redirect('home')
    return render(request,'index.html',{'content':content})



def remove(request,id):
    if request.method=='POST':
       #take object that curesponding to the id and delete it.
        word_count.objects.get(id=id).delete()
    return redirect('home')



def favourite(request,id):
    #take object that curesponding to the id
    obj=word_count.objects.get(id=id)
    if request.method=='POST':
        #update fav into True or False
        if obj.fav == 0:
            word_count.objects.filter(id=id).update(fav=True)
        else:
            word_count.objects.filter(id=id).update(fav=False)
    return redirect('home')