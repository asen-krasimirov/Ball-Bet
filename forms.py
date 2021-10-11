from wtforms import Form, StringField


class ContactForm(Form):
    sender_email = StringField('Email')
    message_content = StringField('Message')
