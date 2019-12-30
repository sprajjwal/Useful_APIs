import smtplib 
import os

class sendGmail:
    """ Main class that sends emails """
    def __init__(self,username:str, password:str):
        """ init method that sets up smtp. takes in
        username and password for a gmail account. """
        self.username = username
        self.password = password

        try:
            # creates SMTP session 
            self.s = smtplib.SMTP('smtp.gmail.com', 587)

            self.s.ehlo()

            # start TLS for security 
            self.s.starttls() 

            # Authentication 
            self.s.login(self.username, self.password) 
        except Exception as e:
            print("*****************************************")
            print("FAILED TO LOGIN, CHECK YOUR CREDENTIALS.")
            print("*****************************************")

    def send(self, receivers:list, message:str, subject="") -> bool:
        """ Sends email in the format
        {subject}
        Hi {receiver},
        {message}

        Cheers,
        
        Returns False if any mail raises error"""

        # type tests
        assert type(receivers) == list
        assert type(message) == str

        is_fail = False

        # message construction and emails being sent
        for receiver in receivers:

            # message to be sent 
            message = f"""\
Subject: {subject}


Hi {receiver},
{message}

Cheers"""

            # sending the mail 
            if self.s.sendmail(self.username, receiver, message) != {}:
                is_fail = True
        
        return is_fail


if __name__ == "__main__":

    a = sendGmail('TEST_USERNAME', 'TEST_PASSWORD')
    print(a.send(['TEST_RECEPIENT_1'], 'test', 'test subject'))