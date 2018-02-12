if [[ $APP_ENV == 'STAGING' ]] || [[ $APP_ENV == 'PROD' ]]; then
 # Check that the environment variable has been set correctly
 if [ -z "$SECRETS_BUCKET_NAME" ]; then
   echo >&2 'error: missing SECRETS_BUCKET_NAME environment variable'
   exit 1
 fi
 export $(aws s3 cp s3://${SECRETS_BUCKET_NAME}/env.txt - | sed 's/^/export /' | xargs) > /dev/null
fi

python manage.py migrate                  # Apply database migrations
python manage.py loaddata tasks.json      # Load tasks fixture

if [[ $APP_ENV == 'STAGING' ]] || [[ $APP_ENV == 'PROD' ]]; then
   python manage.py compilescss
   python manage.py collectstatic --noinput
fi

if [[ $APP_ENV == 'DEV' ]]; then
   python manage.py runserver 0.0.0.0:8000
else
   uwsgi --ini uwsgi.ini
fi
