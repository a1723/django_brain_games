### Установка и запуск проекта:
```bash
git clone https://github.com/a1723/django_brain_games && cd django_brain_games
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cd project && python manage.py migrate
python manage.py makemigrations brain_games
python manage.py runserver
```
Visit http://127.0.0.1:8000




### TO-DO:
<<<<<<< Updated upstream
- How can i send "name" from one views to template and to another view ? Using models ?!!!
=======
<del> How can i send "name" from one views to template and to another view ? Using models ?!!! </del>
>>>>>>> Stashed changes
- make design
- name can't be empty (check it in model ?)
- Make single template for all games
- Make class for each game methods ? 
