# 최적의 클린로드 시스템 위치 선정
####1. 조번호, 조원 : 11팀, 안여진, 김고은, 김수지

####2. 프로젝트 개요 
##### 연구 문제: 최적의 클린로드 시스템 운영을 위한 위치 선정
##### 연구 목표 : 열섬현상이 심각한 지역을 뽑아 클린로드 시스템 설치가 필요한 지역 선정
-> 열섬현상은 미세먼지 농도, 녹지 면적, 생활인구수, 교통량 등의 다양한 요인에 영향을 받음

-> 여러 데이터를 전처리 및 취합해 최적의 위치 선정


####3. 코드 실행 방법 및 구조
#####  데이터 시각화
main branch의 Run 패키지에 있는 visualizaion.py 코드를 실행시키면 시각화된 그래프 확인 가능

##### 데이터 전처리
main branch의 preprocessing 패키지에 있는 people_code, trans_code를 실행시키면 전처리 완료된 데이터를 얻을 수 있음

####4. 발전시킨 내용
##### 데이터 전처리
전처리가 미흡했던 데이터에 대해서 간단한 코드를 이용해 전처리완료
-> 생활인구수 데이터
-> 교통량 데이터

##### 데이터 시각화
*사용한 데이터
-> 자치구별 7,8월 평균 미세먼지 농도 데이터
-> 자치구별 녹지 면적 데이터

##### 그래프 시각화
-> matplotlib을 사용하여 각 자치구별 미세먼지 농도, 녹지 면적을 정렬하여 그래프출력


####5. 기타 특이사항
-
