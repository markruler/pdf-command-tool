# Tk for PDF

## 실행

```shell
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

```shell
python tkinter_windows.py
```

## 설치

```shell
pip install pyinstaller
```

- `--onefile` 옵션은 하나의 실행 파일로 묶는다.
- GUI 프로그램을 빌드할 때는 `--windowed` 옵션을 추가한다.

```shell
pyinstaller --onefile --windowed tkinter_windows.py
```
