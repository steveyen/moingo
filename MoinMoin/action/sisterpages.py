# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - "sisterpages" action

    This action generates a list of page urls and page names, so that other wikis
    can implement SisterWiki functionality easily.
    See: http://usemod.com/cgi-bin/mb.pl?SisterSitesImplementationGuide

    @copyright: 2007 MoinMoin:ThomasWaldmann
    @license: GNU GPL, see COPYING for details.
"""

import time

from MoinMoin import wikiutil
from MoinMoin.Page import Page
from MoinMoin.util import timefuncs
from MoinMoin.logfile import editlog

def execute(pagename, request):
    log = editlog.EditLog(request)
    try:
        lastmod = wikiutil.version2timestamp(log.date())
    except:
        lastmod = 0

    timestamp = timefuncs.formathttpdate(lastmod)
    etag = "%d" % lastmod

    # for 304, we look at if-modified-since and if-none-match headers,
    # one of them must match and the other is either not there or must match.
    if request.if_modified_since == timestamp:
        if request.if_none_match:
            if request.if_none_match == etag:
                request.emit_http_headers(["Status: 304 Not modified"])
        else:
            request.emit_http_headers(["Status: 304 Not modified"])
    elif request.if_none_match == etag:
        if request.if_modified_since:
            if request.if_modified_since == timestamp:
                request.emit_http_headers(["Status: 304 Not modified"])
        else:
            request.emit_http_headers(["Status: 304 Not modified"])
    else:
        # generate an Expires header, using 1d cache lifetime of sisterpages list
        expires = timefuncs.formathttpdate(time.time() + 24*3600)

        httpheaders = ["Content-Type: text/plain; charset=UTF-8",
                       "Expires: %s" % expires,
                       "Last-Modified: %s" % timestamp,
                       "Etag: %s" % etag, ]

        # send the generated XML document
        request.emit_http_headers(httpheaders)

        baseurl = request.getBaseURL()
        if not baseurl.endswith('/'):
            baseurl += '/'

        # Get list of user readable pages
        pages = request.rootpage.getPageList()
        pages.sort()
        for pn in pages:
            p = Page(request, pn)
            entry = u"%s %s\r\n" % (request.getQualifiedURL(p.url(request)), p.page_name)
            request.write(entry.encode('utf-8'))
