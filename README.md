# unstructured

## 핵심: 문서등을 분석해서 llm 작업을 위한 전처리된 DATA 제공
***
문서를 llmdpd에 잘 작동하는 방식으로 전환하는 기능
테이블 제목 리스트 모두 따로 분리해서 이해
각 중요도에 따라 레버리지 설정 가능 (랭체인 사용)
***

각 부분의 언어, 페이지 번호, 메타데이타 , 타입, 이런 태그 정보를 json 형식으로 제공한다.
이걸 랭체인에 넣어서 학습시켜서 llm 을 내가 원하는 어플리케이션 형태로 만드는 것 가능하다.
예를들어 내가 신탁계약서의 키 밸류를 뽑는 llm 어플리케이션을 만들고 싶다면 그에 적합한 백터데이터 json파일을 제공할 수 있다는 것
![image](https://github.com/Madung2/unstucturedio_test/assets/104334219/af9759b4-dd5f-4423-9857-beec04223e0d)

filename: 파일 이름
file_directory: 파일 디렉토리
last_modified: 마지막 수정 날짜
filetype: 파일 유형
coordinates: XY 경계 상자 좌표
parent_id: 요소 계층 구조
category_depth: 동일 카테고리의 다른 요소와 비교한 요소의 깊이
text_as_html: 추출된 표의 HTML 표현
languages: 문서 또는 요소의 언어
emphasized_text_contents: 원본 문서의 강조 텍스트(볼드 또는 이탤릭)
emphasized_text_tags: 원본 문서의 강조된 텍스트에 대한 태그
is_continuation: 요소가 이전 요소의 연속인지 여부
detection_class_prob: 탐지 모델 클래스 확률
기타 유로 버전은 PDF나 이미지 파일 OCR 기능을 제공
