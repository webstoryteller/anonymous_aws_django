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

   
