import boto3
from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()

s3 = boto3.client("s3")
BUCKET_NAME = "bakketo-7779"


@router.post("/uploads")
def uploading_file(uploadfile: UploadFile = File(...)):
    img_type = ["image/jpg", "image/jpeg", "image/heic", "image/png"]
    if uploadfile.content_type not in img_type:
        raise HTTPException(detail="invalid datatype", status_code=402)
    file_content = uploadfile.file.read()
    file_storage = len(file_content)
    if file_storage > 2 * 1024 * 1024:
        raise HTTPException(detail="the size is too large", status_code=403)

    s3_key = f"uploads/{uploadfile.filename}"
    s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=file_content)

    return {
        "detail": "its passed new cd here all the way ",
        "file_name": uploadfile.filename,
        "filesize": file_storage,
    }
