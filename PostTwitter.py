import tweepy as tw
import gpt_2_simple as gpt2
import time
# --------------------------------------------------AUTHORIZING---------------------------------------------

# fill in twitter api auth data here
cons_key = ''
cons_secr = ''
access_tok = ''
access_secr = ''

auth = tw.OAuthHandler(cons_key, cons_secr)
auth.set_access_token(access_tok, access_secr)
api = tw.API(auth)

try: 
    test = api.home_timeline()
except tw.TweepError as e:
    print('Check authentication data')
    print(f'Error message: {e.response.text}')
    exit()


# ------------------------------------------------------------------------------------------------------------


def tweet():
    print('generating tweet')
    try:
        res = gpt2.generate(sess, run_name='twitter-run', length=300, truncate='<|endoftext|>', prefix='<|startoftext|>', include_prefix=False, return_as_list=True)[0]
        if u'...' in res:
            print('found ..., regenerating')
            tweet()
        else:
            api.update_status(res)
            print('succesfully tweeted')
    except tw.TweepError as e:
        print(e)
        if e.api_code == 187:
            tweet()

print('starting session')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='twitter-run')
print('session started succesfully')
starttime=time.time()
while True:
  tweet()
  time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))