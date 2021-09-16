# blog_django
## 1) Crear y activar el entorno virtual:
```python
  py -m venv venv
  cd venv/Scripts/
  activate
```  
## 2) Instalar las dependencias del proyecto
```python
   pip install -r requirements.txt
``` 
## 3) Crear y configurar la base de datos desde el archivo settings.py ubicado en la carpeta del proyecto blog_django
```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'blog_djangodb',
            'USER': 'my_user',
            'PASSWORD': 'my_password',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
```  
## 4) Realizar las migraciones
```python
    python manage.py makemigrations
    python manage.py migrate
```
## 5) Crear la cuenta del super usuario (opcional)
```python
    python manage.py createsuperuser
```
## 6) Correr el servidor de Django
```python
    python manage.py runserver
```
