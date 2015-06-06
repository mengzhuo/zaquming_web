#!/usr/bin/env python
# encoding: utf-8
import logging
logger = logging.getLogger(__name__)

from bottle import request

request_logger = logging.getLogger('request.params')

def logplugin(callback):

    def wrapper(*args, **kwargs):
        request_logger.info(request.params)
        body = callback(*args, **kwargs)
        request_logger.info(body)
        return body

    return wrapper

