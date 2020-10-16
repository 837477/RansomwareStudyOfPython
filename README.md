# Ransomware Study - Python
> 지정된 경로의 모든 파일을 특정 암호화 알고리즘으로 파일을 암호화한다.

파이썬을 처음 공부하고 있던 시점에서 구현한 프로그램입니다.

기존 C기반의 랜섬웨어 스터디에서 Python 언어를 공부하면서 같은 기능을 그대로 Python으로 구현했습니다. 더불어 기존 C기반의 랜섬웨어의 암호화 알고리즘은 본인이 임시적으로 만든 수학 식이었으나, 본 Python 버전의 랜섬웨어는 외부 라이브러리를 사용하여 구현했습니다.

![837477](./rdm/837477.png)

## Installation

OS X & Linux:

```sh
git clone https://github.com/837477/RansomwareStudyOfPython.git
```

Windows:

```sh
git clone https://github.com/837477/RansomwareStudyOfPython.git
```



## Usage example

본 디렉토리에는 두 개의 파일이 존재합니다.

- encrypt.c (암호화)
- decrypt.c (복호화)

암호화 / 복호화 를 진행하기전에 암호화 대상의 경로를 필수로 두 파일의 main함수에서 지정해주어야 합니다.  

```python
target_local = desktopPath + '\\desktop'
```

암호화 대상 확장자를 Custom 할 수 있습니다.

```python
if Extension in ['.hwp', '.txt']:
# or
if Extension not in ['.hwp', 'txt'] # 권장하지 않음.
```



## Development setup

이번 Python 버전의 랜섬웨어(학습용)은 외부 암호 알고리즘이 사용되었으며, 아래의 라이브러리를 설치하시길 바랍니다.

```sh
pip install AES
pip install hashlib
```



## Release History

* 0.0.1
    * Work in progress



## Meta

🙋🏻‍♂️ Name: 837477 

📧 E-mail: 8374770@gmail.com

📔 Blog: http://837477.pythonanywhere.com

🐱 Github: https://github.com/837477



## Contributing

1. Fork it (<https://github.com/837477/RansomwareStudyOfPython>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
