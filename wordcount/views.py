from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def count(request):
    text=request.GET['fulltext']
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sortedwords = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'text':text, 'total':len(word_list), 'sortedwords':sortedwords})
