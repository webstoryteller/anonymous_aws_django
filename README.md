장고 django AWS 배포 성공 과정

(1) 개발 환경. (패키지, 프로그램 버전 등)
 - python 3.13.7
   
 - requirements
   
    django==4.2.24
   
    psycopg

    psycopg-binary

    boto3

    django-storages

    awsebcli


   주의 :


   psycopg2, psycopg2-bnary 아님. postgre sql 드라이버인데 2025년 5월에 psycopg3 업데이트 올라옴. psycopg2로 올리면 AWS에 신규 배포하려고 하면 에러가 남. 그래서 자동 최신 버전 받으려면 psycopg, psycopg-binary로 입력해야 함.


  django는 AWS ssh로 접속해 설치 과정에서 최신 버전을 4.2.24까지만 표시한 것을 보았음. django 5.0 이상 버전 썼다가 배포 에러가 나서 4.2.24로 다시 설치하고 코딩하여 배포했더니 성공함.

☆★☆ 오류 error 해결 방법
1) 가상 venv 설치 할 때 에러 메시지 Activate.ps1 is published by CN=Python Software Foundation, O=Python Software Foundation, L=Beaverton, S=Oregon, C=US and is not trusted on your system. Only run scripts from trusted publishers.
 >>> To fix the "script is not trusted" error for activate.ps1, you must either temporarily change your PowerShell execution policy to RemoteSigned or Unrestricted for the current session, import the certificate from the Python Software Foundation into your Trusted Publishers store, or use cmd.exe instead of PowerShell to run the activation script. 


PowerShell 실행 정책 변경은 관리자 권한으로 PowerShell을 실행한 후 Set-ExecutionPolicy cmdlet을 사용하여 변경하며, Get-ExecutionPolicy -List 명령으로 현재 설정을 확인하고 Set-ExecutionPolicy <정책 이름>으로 변경합니다. 


powershell 화면 : Get-ExecutionPolicy -List

powershell 화면 : Set-ExecutionPolicy RemoteSigned

이 명령을 실행하면 변경 내용을 적용할지 묻는 메시지가 나타날 수 있으며, 'Y'를 입력하여 승인합니다. 


2) postgre DB 연결 드라이버 설정

psycopg2는 웹 배포 때 에러가 나므로 psycopg3로 업그레이드하는데 다음 두 가지 방법 적용

 - requirements.txt에 추가

psycopg

psycopg-binary


- 가상 환경에서 psycopg 3 관련 패키지를 한 번에 설치
- 
명령어 : pip install "psycopg[binary]"


3) VS code 가상 환경 select interpreter 단축키 : F1


4) cp949 에러 관련 사항. utf 8 관련

제어판 > 시계 및 국가 > 국가 또는 지역 > 관리 탭 > 시스템 로캘 변경

"Beta: 세계 언어 지원을 위해 Unicode UTF-8 사용" 옵션 체크

컴퓨터 재시작

출처: https://coding-shop.tistory.com/472 [끄적끄적 코딩 공방:티스토리]


5) Dbeaver postgres 연결 시 전체 데이터베이스 안 보임
   
Databases 오른쪽 마우스  - Edit Connection (단축키 F4) - 팝업창에서 Show all databases 체크 표시


6) database user 테이블 필드 지정할 때 대소문자 구분하므로 주의할 것. Nickname은 nickname과 다름


7) 장고 django default storage 를 AWS S3로 변경

settings.py에 다음과 같이 입력할 것. 장고 특정 버전에서 DEFAULT_FILE_STORAGE 설정은 안 됨.

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


STORAGES = {

    "default": {
    
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage", # Amazon S3 백엔드 사용
        
    },
    
    "staticfiles": {
    
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        
    },
    
}



8) 웹 URL 입력시 에러 관련 사항

장고 django 특정 버전 이상에서 default_storage의 3 저장 경로 URL의 정규화 기능 관련 사항

"AWS-example.com" 이렇게 변수로 입력하면 django는 "/"를 자동으로 붙이는 경우가 있으므로 주의할 것. "AWS-example.com/"

board/views.py 의 구문

img_url = f"/upload/{img_name}.{ext}" => AWS-example.com///upload/{img_name}.{ext}

에러가 남.

아래처럼 고칠 것.

img_url = f"upload/{img_name}.{ext}"



★☆★ AWS 실제 배포 명령어 출력

(venv) PS C:\project\ANONYMOUS> eb init


Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : EU (Ireland)
5) eu-central-1 : EU (Frankfurt)
6) ap-south-1 : Asia Pacific (Mumbai)
7) ap-southeast-1 : Asia Pacific (Singapore)
8) ap-southeast-2 : Asia Pacific (Sydney)
9) ap-northeast-1 : Asia Pacific (Tokyo)
10) ap-northeast-2 : Asia Pacific (Seoul)
11) sa-east-1 : South America (Sao Paulo)
12) cn-north-1 : China (Beijing)
13) cn-northwest-1 : China (Ningxia)
14) us-east-2 : US East (Ohio)
15) ca-central-1 : Canada (Central)
16) eu-west-2 : EU (London)
17) eu-west-3 : EU (Paris)
18) eu-north-1 : EU (Stockholm)
19) eu-south-1 : EU (Milano)
20) ap-east-1 : Asia Pacific (Hong Kong)
21) me-south-1 : Middle East (Bahrain)
22) af-south-1 : Africa (Cape Town)
23) ap-southeast-3 : Asia Pacific (Jakarta)
24) ap-northeast-3 : Asia Pacific (Osaka)
25) il-central-1 : Israel (Tel Aviv)
26) me-central-1 : Middle East (UAE)
(default is 3): 10


Select an application to use
1) Test
2) [ Create new Application ]
(default is 2): 2


Enter Application Name
(default is "ANONYMOUS"):
Application ANONYMOUS has been created.

It appears you are using Python. Is this correct?
(Y/n): y
Select a platform branch.
1) Python 3.13 running on 64bit Amazon Linux 2023
2) Python 3.12 running on 64bit Amazon Linux 2023
3) Python 3.11 running on 64bit Amazon Linux 2023
4) Python 3.9 running on 64bit Amazon Linux 2023
(default is 1):

Do you want to set up SSH for your instances?
(Y/n):

Select a keypair.
1) aws-anonymous-key
2) anonymous-key
3) [ Create new KeyPair ]
(default is 2): 1

(venv) PS C:\project\ANONYMOUS_7> eb create
Enter Environment Name
(default is ANONYMOUS-dev): 
Enter DNS CNAME prefix
(default is ANONYMOUS-dev): 

Select a load balancer type
1) classic
2) application
3) network
(default is 2): 2


Would you like to enable Spot Fleet requests for this environment? (y/N): n
Creating application version archive "app-.....".
Uploading 
.
.
.
2025-09-25 13:57:48    INFO    Instance deployment successfully generated a 'Procfile'.
2025-09-25 13:57:52    INFO    Instance deployment completed successfully.
2025-09-25 13:58:07    INFO    Application available at ANONYMOUS-...
2025-09-25 13:58:07    INFO    Successfully launched environment: ANONYMOUS-...

(venv) PS C:\...\ANONYMOUS> 

   
