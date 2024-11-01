echo "Build Start"
python -m pip install requirements.txt
python manage.py collectstatic --noinput --clear
echo "Build End"