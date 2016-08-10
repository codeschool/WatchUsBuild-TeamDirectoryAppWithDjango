# WatchUsBuild-TeamDirectoryAppWithDjango - PART 2
__Part 2__ of the Code for the Directory app built during the Watch Us Build screencast.

__Note__ we deleted our key and secret from our google developer's console so you can create your own here:
https://console.developers.google.com
Then replace the key and secret variables with your values:
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


Currently this app has some dependencies required to deploy it to Heroku that need to be installed before it will run locally.  The dependencies are:
* `Django==1.10`
* `gunicorn==19.6.0`
* `whitenoise==3.2`
* `python-social-auth`

Those can be installed from the `requirements.txt` file with the following command - `pip install -r requirements.txt`.  Or they can be installed separately with `pip`.
