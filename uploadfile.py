from fastapi import FastAPI,HTTPException,UploadFile,File,Depends,APIRouter
import os

router=APIRouter()
os.makedirs('uploads',exist_ok=True)
@router.post('/uploadfile')
def upload_file(files:UploadFile=File(...)):
    img_type=['image/jpeg','image/png','image/heic']
    if files.content_type not in img_type:
        raise HTTPException(detail=('invalid image type'),status_code=403)
    inside_file=files.file.read()
    total_storage=len(inside_file)
    if total_storage>2*1024*1000:
        return 'file size too large'
    file_location=f'uploads/{files.filename}'
    with open(file_location,'wb')as f:
        f.write(inside_file)
        return {'message':'its sucessful','file_name':files.filename,'file_storage':total_storage}





