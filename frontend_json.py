#!/usr/bin/env python

# Copyright (c) 2009 Johan Uhle
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from django.utils import simplejson as json

import logging

import os
import urllib

import models
import utils
import settings

class MainHandler(webapp.RequestHandler):
	"""
	This script returns JSON-formatted tracks.
	"""
	
	def get(self):
		genre = (self.request.uri).split('/')[-1]
		
		if genre == 'rock': tracks = models.TrackCache.gql("WHERE genre = :1 ORDER BY __key__ DESC LIMIT "+str(settings.FRONTEND_TRACKS_LIMIT), "rock")
		elif genre == 'techno': tracks = models.TrackCache.gql("WHERE genre = :1 ORDER BY __key__ DESC LIMIT "+str(settings.FRONTEND_TRACKS_LIMIT), "techno")
		elif genre == 'house': tracks = models.TrackCache.gql("WHERE genre = :1 ORDER BY __key__ DESC LIMIT "+str(settings.FRONTEND_TRACKS_LIMIT), "house")
		else: tracks = models.TrackCache.gql("ORDER BY __key__ DESC LIMIT "+str(settings.FRONTEND_TRACKS_LIMIT))
		
		track_array = []
		used_locations = set()
		for track in tracks:
			# a distinct location may only be on the map once because marker on same position aren't displayed properly
			location = str(track.location_lat) + "/" + str(track.location_lng)
			if location in used_locations: continue
			used_locations.add(location)
			
			location_track_counter = models.LocationTracksCounter.get_by_key_name(location)																											
			
			track_array.append({  'track_id' : track.track_id,
														'title' : track.title,
														'permalink' : track.permalink,
														'username' : track.username,
														'avatar_url' : track.avatar_url,
														'location_lng' : track.location_lng,
														'location_lat' : track.location_lat,
														'tracks_in_location' : getattr(location_track_counter, 'counter', 1), 
														'created_at' : "new Date(\"%s\")" % track.created_at.ctime(),
														'created_minutes_ago' : track.created_minutes_ago(),
														'waveform_url' : track.waveform_url})
														
		tracks_json = json.dumps(track_array)
		self.response.out.write(tracks_json)

def main():
  application = webapp.WSGIApplication([('/frontend-json/', MainHandler),
																				('/frontend-json/.*', MainHandler),], debug=utils.in_development_enviroment())
  run_wsgi_app(application)

if __name__ == '__main__':
  main()