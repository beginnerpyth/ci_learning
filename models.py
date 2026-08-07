from fastapi import FastAPI,HTTPException
from database import base,settings,db,tablemaker
from sqlalchemy import Table,Integer,Column,String,create_engine
from sqlalchemy.orm import DeclarativeBase



class register_class(base):
    course_name:str
    course_id:int
    day:str

class student_register(base):
    student_name:str
    student_id:int
class student_update(base):
    student_name:str
    student_id:int

class student_database(tablemaker):
    __tablename__='Student_db'
    student_name=Column(String)
    student_id=Column(Integer,primary_key=True)


class teacher_database(tablemaker):
    __tablename__='Teacher_db'
    teacher_name=Column(String)
    teacher_id=Column(Integer,primary_key=True)



