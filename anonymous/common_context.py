from django.conf import settings

def img_url_context(request):
    # return {"IMG_URL":settings.S3_ROOT_URL}
    return {"IMG_URL":f"{settings.S3_ROOT_URL}/"} # 장고 django 특정 버전 이상에서는 / 를 주의해서 붙여야 함. ----.com/upload/----.png. ---.com 으로 경로 입력하면 자동으로 ---.com/ 으로 인식하는 기능 때문임

def project_name_context(request):
    # return {"IMG_URL":settings.S3_ROOT_URL}
    return {"PROJECTNAME":{settings.PROJECT_NAME}}