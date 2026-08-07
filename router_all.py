from fastapi import FastAPI,HTTPException,APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import token_decoder,token_creator,token_verifier
from models import register_class,student_register,student_update
from uploadfile import upload_file
from models import student_database,teacher_database
from services import service
from database import db
from sqlalchemy.orm import Session

router=APIRouter()


fake_database={1:{'day':'sunday','course_name':'math'}}
@router.post('/login')
def login(form_layout:OAuth2PasswordRequestForm=Depends()):
    if form_layout.username=='teacher' and form_layout.password=='teacher123':
        token_created_teacher=token_creator({'email':'teacher@universal.com','name':'uni_teacher','role':'teacher'})
        return {'access_token':token_created_teacher,'token_type':'bearer'}
    if form_layout.username=='student' and form_layout.password=='student123':
            token_created_student=token_creator({'email':'student@universal.com','name':'uni_student','role':'student'})
            return {'access_token':token_created_student,'token_type':'bearer'}
    
    raise HTTPException('there is something wrong with credentials')


@router.get('/only_for_students')
def students(student:str=Depends(token_verifier('student'))):
    return f'only {student} can access this'

@router.get('/only_for_teachers')
def teacher(teacher:str=Depends(token_verifier('teacher'))):
    return f'only {teacher} can access this'

@router.post('/register_the_course')
def course_register(class_schedule:register_class,teacher:str=Depends(token_verifier('teacher'))):
    if class_schedule.course_id in fake_database:
        raise HTTPException(status_code=400,detail='its already registered')
    fake_database[class_schedule.course_id]={'day':class_schedule.day,'course_name':class_schedule.course_name}
    return {'data saved':fake_database[class_schedule.course_id]}


@router.get('/get_student_data')
def student_data(id:int):
     return service.get_id(id)

@router.post('/post_new_student')
def student_post_data(student_post:student_register):
     return service.post_id(student_post)
@router.put('/change_student_data')
def student_change_data(update_name:student_update):
     return service.update_data(update_name)

     student_db_creator=[{'student_id':x,'student_name':'student'*x} for x in range(1,100)]





@router.get('/pagination')
def pagination(search:str,limit:int=1,size:int=10,db_create:Session=Depends(db)):
     
     skip=(limit-1)*size
     select_table=db_create.query(student_database)
     select_table_filter=select_table.filter(student_database.student_name.contains(search))
     select_table_count=select_table_filter.count()
     select_table_result=select_table_filter.offset(skip).limit(limit).all()
     return{'searched_data':search,
            'skip':skip,
            'limit':limit,''
            'size':size,
            'final_output':select_table_result}






     


          




