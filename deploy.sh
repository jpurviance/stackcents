heroku config:set DISABLE_COLLECTSTATIC=0
git push heroku master
heroku config:unset DISABLE_COLLECTSTATIC
