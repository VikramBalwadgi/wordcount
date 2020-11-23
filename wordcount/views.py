# from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def counts(request):
    full_text = request.GET['fulltext']
    wordcount = len(full_text.split())
    xyz = full_text.split()
    worddict = {}
    for word in xyz:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sort_wordlist = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'counts.html',
                  {'fulltext': full_text, 'word_count': wordcount, 'worddict': sort_wordlist})

def about(request):
    return render(request, 'about.html')
