#!/bin/sh

# Wait for dependencies to be ready (if needed)
echo "Starting application..."

# Apply database migrations
python manage.py migrate

# Create default database if not exists
if [ ! -f "/app/db/db.sqlite3" ]; then
  touch /app/db/db.sqlite3
  chmod 644 /app/db/db.sqlite3
  python manage.py migrate
fi

# Create superuser if needed (for development)
if [ "$CREATE_SUPERUSER" = "1" ]; then
  python manage.py createsuperuser --noinput
fi

# Start server
exec "$@"