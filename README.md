# Excel Merge Studio

여러 개의 엑셀 파일(.xlsx, .xls)을 업로드하면 하나의 통합 엑셀 파일로 자동 병합해 주는 간단한 웹 앱입니다.

## 실행 방법

1. VS Code에서 이 폴더를 열기
2. [index.html](index.html) 파일을 열기
3. VS Code의 Live Server 확장으로 열거나 아래 명령으로 간단히 실행하기

```bash
cd C:\Users\세미\excel-merge-app
python -m http.server 8000
```

4. 브라우저에서 http://localhost:8000 접속

## 특징

- 여러 파일 동시 업로드
- 드래그 앤 드롭 지원
- 파일별 삭제 기능
- 첫 번째 시트 기준 자동 병합
- 출처 파일명 열 자동 추가
- 중복 행 제거 옵션
- 통합 엑셀 다운로드
