from database import settings
from fastapi.testclient import TestClient
import services
import pytest
from main import app
import router_all
saved=[]



@pytest.fixture(autouse=True)
def test_clear():
     
     router_all.fake_database.clear()
     router_all.fake_database[1]={'day':'sunday','course_name':'math'}



client=TestClient(app)

#def test_login():
#    test_log=client.post('/login?form_layout.username=student&formlayout.password=student123')
#    assert test_log.json()==
    





    

def test_one():
   a=2
   b=3
   assert a+b==5


def test_log():
    test_token=client.post('/login',data={'username':'student','password':'student123'})
    #OAuth2PasswordRequestForm expects the username/password as form data.
    token=test_token.json()['access_token']
    test_studs=client.get('/only_for_students',headers={'Authorization':f'bearer {token}'})
    assert test_token.status_code == 200
    assert test_studs.json() == 'only student can access this'#OAuth2PasswordRequestForm expects the username/password as form data.
    assert test_studs.status_code == 200





