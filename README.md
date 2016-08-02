# WatchUsBuild-TeamDirectoryAppWithDjango
Code for the Directory app built during the Watch Us Build screencast.

Currently this app has some dependencies required to deploy it to Heroku that need to be installed before it will run locally.  The dependencies are:
* `Django==1.10`
* `gunicorn==19.6.0`
* `whitenoise==3.2`

Those can be installed from the `requirements.txt` file with the following command - `pip install -r requirements.txt`.  Or they can be installed separately with `pip`.
