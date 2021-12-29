#LCU code base


## Project struct

```markdown

    -Practice
        --alembic
            ---version              #define migrate files
            ---env.py               #config run migrations
        --LCU
            ---controllers          
            ---models
            ---serializers
            ---views.py             #define viewset
        --Practice
            ---settings.py
            ---urls.py
        --base.py                   #define connection
        --requirements.txt          #lib
```                    

##setup: 
```commandline
pip3 install -r requirements.txt 
```

##database:

Change in connection string `base.py`

example:
```python
engine = sa.create_engine('oracle://minhdt:minhdt123@localhost:1521/ORCLCDB', echo=True)
```

with 
```commandline
oracle://username:password@domain:port/SID
```

##Migrate
```commandline
alembic revision --autogenerate -m 'name file'
```

##Start server
```commandline
python3 manage.py runserver
```

