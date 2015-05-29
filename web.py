#!/usr/bin/env python
# encoding: utf-8

from urllib import quote

from plugins import logplugin

from bottle import (route, run, view, HTTPError,
                    install, request, HTTPResponse)
import db
db.init()
install(logplugin)

from models import Word, TransLation
from mongoengine import DoesNotExist, NotUniqueError


@route('/')
@view('index.html')
def index():
    lastest_word = Word.objects.order_by('update_at')[0]
    highest_word = Word.objects.order_by('rating')[0]
    return dict(lastest_word=lastest_word,
                highest_word=highest_word)


@route('/w/<name>')
@view('word_detail.html')
def show_word(name):

    try:
        word = Word.objects.get(name=name, blocked=False)
    except DoesNotExist:
        raise HTTPError(404, "Word %s not found" % name)

    return dict(word=word)

@route('/add', method=['post', 'get'])
@view('add_word.html')
def add_word():
    
    name = request.params.name.replace(" ", '')
    trans = request.params.tranlation.strip()
    
    if name and trans:
        try:
            w = Word(name=name)
            w.trans.append(TransLation(name=trans))
            w.save()
        except NotUniqueError:
            pass

    return HTTPResponse(status=303,
                        headers=[('Location', '/w/%s' % quote(name.encode('utf8')))])

@route('/update')
@view('update_word.html')
def update_word():
    pass

@route('/search')
@view('search.html')
def search_word():
    query_name = request.params.q
    if query_name:
        words = Word.objects.filter(name__icontains=query_name)
        return dict(words=words, query_name=query_name)
    else:
        raise HTTPError(400, "No params")

if __name__ == '__main__':
    run(host='0.0.0.0', port=5000, reloader=True, debug=True)
