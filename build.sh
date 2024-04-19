#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

python manage.py collectstatic --no-input
python manage.py migrate