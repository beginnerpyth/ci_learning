from fastapi import FastAPI,HTTPException
from models import student_register,student_update
fake_student_db={1:'abhishek',2:'takahashi'}
class Service():
    def get_id(self,id:int):
        if id in fake_student_db:
                    return f'student with data is already saved {fake_student_db[id]}'
        raise HTTPException(status_code=404,detail='data not here')
    def post_id(self,post_layout:student_register):
         if post_layout.student_id in fake_student_db:
               return f'student with data is already saved {fake_student_db[post_layout.student_id]}'
         fake_student_db[post_layout.student_id]=post_layout.student_name
         return f'this data {fake_student_db[post_layout.student_id]} is saved'
        
    def update_data(self,update_layout:student_update):
          check_data_update=self.get_id(update_layout.student_id)
          if check_data_update:
                fake_student_db[update_layout.student_id]=update_layout.student_name

          return f'this data {fake_student_db[update_layout.student_id]} is changed'
          

service=Service()



                
          
