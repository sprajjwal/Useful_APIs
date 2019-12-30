# GMAIL API (using smtplib)

This python module sends emails to one or several people. This module uses the ***smtplib*** that comes with python.

You are also going to need a working gmail account to send emails from for this.

You will also need to turn [less secure](https://www.google.com/settings/security/lesssecureapps) apps on for you google account on.

## It is important to note that you don't have a file named email.py in your directory as ***smtplib*** uses that

## Usage

Start with setting up the `sendGmail` class object.

    emailer = sendGmail("Username", "Password")

Once this is done, an email can be easily sent by using the `send()` method that takes in 3 arguments.

    emailer.send(['TEST_RECEPIENT_1'], 'MESSAGE', 'SUBJECT')

- Recipeints (required): a list containing all recipients.
  
- Message (required): a string type that contains the message to be sent.

- Subject (not required): a string type subject for the email.
