import zipfile
import os

def 압축하기(경로, 파일명):
    압축파일 = 파일명 + ".zip"
    with zipfile.ZipFile(압축파일, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for 폴더경로, 하위디렉터리, 파일들 in os.walk(경로):
            for 파일 in 파일들:
                파일경로 = os.path.join(폴더경로, 파일)
                zipf.write(파일경로, os.path.relpath(파일경로, 경로))

if __name__ == "__main__":
    경로1 = input("압축할 경로를 입력하세요: ")
    파일1 = input("저장할 파일명을 입력하세요: ")
    
    압축하기(경로1, 파일1)