import os

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()
os.makedirs("new_uploads", exist_ok=True)


@router.post("/uploads")
def uploading_file(uploadfile: UploadFile = File(...)):
    img_type = ["image/jpg", "image/jpeg", "image/heic", "image/png"]
    if uploadfile.content_type not in img_type:
        raise HTTPException(detail="invalid datatype", status_code=402)
    file_content = uploadfile.file.read()
    file_storage = len(file_content)
    if file_storage > 2 * 1024 * 1024:
        raise HTTPException(detail="the size is too large", status_code=403)
    file_path = f"new_uploads/{uploadfile.filename}"
    with open(file_path, "wb") as f:
        f.write(file_content)
        return {
            "detail": "its passed",
            "file_name": uploadfile.filename,
            "filesize": "file_storage",
        }
