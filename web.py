#!/usr/bin/env python
# encoding: utf-8
from gevent import monkey, sleep
monkey.patch_all()

import db
db.init()
from urllib import quote

from plugins import logplugin

from bottle import (route, run, view, HTTPError,
                    install, request, HTTPResponse)
install(logplugin)

from models import Word, TransLation
from mongoengine import NotUniqueError, DoesNotExist

IP_VOTE = {}

@route('/')
@view('index.html')
def index():

    query_name = request.params.q
    if query_name:
        words = Word.objects.filter(name__icontains=query_name)
        return dict(words=words, query_name=query_name)
    else:
        words = []
    
    return dict(words=words, query_name=query_name)

@route('/add', method=['post', 'get'])
@view('add_word.html')
def add_word():
    
    name = request.params.name.replace(" ", '')
    trans = request.params.tranlation.strip()
    if name and trans:
        try:
            w,_ = Word.objects.get_or_create(name=name)
            w.trans.append(TransLation(name=trans))
            w.save()
        except NotUniqueError:
            pass

    return HTTPResponse(status=303,
                        headers=[('Location', '/?q=%s' % quote(name.encode('utf8')))])

@route('/vote', method=['post'])
def vote():
    
    global IP_VOTE
    if len(IP_VOTE) > 3000:
        raise HTTPError(507, "Too many votes")    

    ip = request.remote_addr
    word = request.params.word
    trans = request.params.trans
    vote = request.params.vote
    
    IP_VOTE[ip] = IP_VOTE.get(ip, 0) + 1

    if IP_VOTE[ip] > 30 :
        raise HTTPError(503, "Vote too fast!!")
    try:
        w = Word.objects.get(name=word)
        t = w.trans.get(name=trans)
    except DoesNotExist:
        raise HTTPError(404 ,"Not found")

    if int(vote) > 0:
        t.rating += 1
    else:
        t.rating -= 1

    w.save()
    return dict(vote=vote, trans=t.name)

def reset_vote():
    global IP_VOTE
    while True:
        sleep(30*60)
        IP_VOTE = {} 

if __name__ == '__main__':
    
    run(host='0.0.0.0', port=5000, server='gevent', reloader=False, debug=False)
