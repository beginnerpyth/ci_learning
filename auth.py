from fastapi import FastAPI,HTTPException,Depends
from jose import JWTError,jwt
from fastapi.security import OAuth2PasswordBearer
from  datetime import timedelta,datetime,timezone

token_url=OAuth2PasswordBearer(tokenUrl='/login')
alg='HS256'
time=30
secret_key='mypass'

def token_creator(real_data:dict):
    copy_data=real_data.copy()#only inside dict there is copy()

    exp_time=datetime.now(timezone.utc)+timedelta(minutes=time)
    copy_data.update({'exp':exp_time})#passing the expire data inform of dictionary

    jwt_created=jwt.encode(copy_data,secret_key,algorithm=alg)
    return jwt_created



def token_decoder(real_token:str=Depends(token_url)):
    try:
        copy_token=jwt.decode(real_token,secret_key,algorithms=[alg])
        email=copy_token.get('email')
        name=copy_token.get('name')
        role=copy_token.get('role')
        return {'email':email,'name':name,'role':role}
    except Exception as e:
        print(e)




def token_verifier(real_role:str):#we placed nondefault parameter at first its rule
    def token_compare(token_converter:dict=Depends(token_decoder)):
        if token_converter['role']!=real_role:
            raise HTTPException(status_code=403,detail=(f'you are forbidden as {token_converter["name"]}'))
        return real_role
    return token_compare





    



