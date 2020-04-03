from wtforms import Form, TextAreaField,StringField

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

   ####### 0937319920