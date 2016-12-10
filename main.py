
import webapp2
import random
import os

questionsList = ["How many toes does Isaac have?", "How tall is the average tree?", "On a scale of 1-10 how good is Westworld?"]
answersList = ["10", "6", "8"]

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.write(input-form.html)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)

