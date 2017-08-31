# djsite


start the django webserver
python manage.py runserver 127.0.0.1:8000

python3 manage.py makemigrations
python3 manage.py migrate






python manage.py shell

>>> from news.models import Article
>>> Article.objects.all()

>>> a = Article()
>>> a.headline = "Largest asteroid in 100 years to whizz by Earth on Friday"
>>> a.publish_date = "2017-08-31"
>>> a.content = "Asteroid measures 4.4 kilometres wide – or about the size of 30 Egyptian pyramids stuck together"
>>> a.save()
>>> Article.objects.all()

>>> Article(headline="HK Typhoon",publish_date="2017-08-25",content="A tracking map from the Hong Kong Observatory shows a typhoon making landfall on Sunday afternoon").save()
>>> Article.objects.all()

>>> Article.objects.create(headline="Amazon Alexa-powered robot that can order you a pizza",publish_date="2017-08-30",content="The 2.7-foot robot will go on sale in October for US$2,800, and will be available in English and German. Those are the languages that Alexa currently understands.")


python manage.py createsuperuser
admin.site.register(Model)