#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import string
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

def alphabet_position(char):
    lowerc = string.ascii_lowercase
    upperc = string.ascii_uppercase
    if char in lowerc:
        return lowerc.index(char)
    elif char in upperc:
        return upperc.index(char)

def rotate_character(char, rot):
    lowerc = string.ascii_lowercase
    upperc = string.ascii_uppercase
    if char in lowerc:
        return lowerc[(alphabet_position(char) + rot) %26]
    if char in upperc:
        return upperc[(alphabet_position(char) + rot) %26]

def encrypt(text, rot):
    new = ""
    for c in text:
        if c.isalpha():
            new += rotate_character(c, rot)
        else:
            new += c
    return new

def build_page(textarea_content):
    rot_label = "<label>Rotation Amount:</label>"
    rot_input = "<input type='number' name='rotation'/>"

    msg_label = "<label>Enter a message:</label>"

    textarea = "<textarea name='message'>" + textarea_content + "</textarea>" + "<br>" + "<input type='submit' value='Submit'/>"

    #submit = "<input type='submit'/"

    form = ("<form method='post'>" +
            rot_label + rot_input + "<br>" +
            msg_label + textarea + "</form>")
    header = "<h2>Web Caesar</h2>"
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.out.write(content)

    def post(self):
        message = self.request.get("message")
        message = escape_html(message)
        rotation = int(self.request.get("rotation"))
        encrypted_message = encrypt(message, rotation)
        #content = build_page(encrypted_message)
        self.response.out.write(build_page(encrypted_message))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
