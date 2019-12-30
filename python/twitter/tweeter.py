import os
import tweepy as tw

def str_to_html(msg):
    msg = msg.split(' ')
    html_str = ""
    is_prev_eol = True
    for item in msg:
        if item[0]=='.':
            item = item[1:]
        if is_prev_eol:
            item = item.capitalize()
            is_prev_eol = False
        # test for usernames, add <a>
        if item[0] =='@':
            html_str += f"<a href='https://www.twitter.com/{item}' target='_blank'>{item}</a> "
        elif item[0]=='#':
            html_str += f"<a href='https://twitter.com/search?q=%23{item[1:]}' target='_blank'>{item}</a> "
        elif item[0:4].lower() == 'http':
            html_str += f"<a href='{item}' target='_blank'>{item}</a> "
        else:
            html_str += item + ' '
        # check if orev eol, add caps, set isPrev to false

        #check if word ended in '.', set is prev to true
        if  item[len(item)-1] in'.?!':
            is_prev_eol = True
    html_str = html_str[:len(html_str)-1]
    if html_str[len(html_str)-1].isalnum():
        html_str +='.'
    
    return html_str

def tweet(msg):
    """TWEETS THE MESSAGE TO THE TWITTER ACCOUNT"""
    consumer_key = os.environ['CONSUMER_KEY'] 
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    api.update_status(msg)

if __name__== '__main__':
    test = "-the holiday season is here but that is no excuse not to stay on top of your business prospects. Focus!"
    print(str_to_html(test))