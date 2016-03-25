import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'Home'}))

class EventsHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/events.html')
    	self.response.write(template.render({'title': 'Events'}))

class DesignHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/design.html')
    	self.response.write(template.render({'title': 'Design'}))

class TransitionHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/before-after.html')
        self.response.write(template.render({'title': 'Before and After'}))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render({'title': 'About'}))
            
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/events.html', EventsHandler),
    ('/design.html', DesignHandler),
    ('/before-after.html', TransitionHandler),
    ('/about.html', AboutHandler)
], debug=True)
