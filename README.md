# Ransomware_Study

> 지정된 경로의 모든 파일을 특정 암호화 알고리즘으로 파일을 암호화한다.



파이썬을 처음 공부하고 있던 시점에서 구현한 프로그램입니다.

이미 알고 있는 C언어를 기반으로 랜섬웨어의 원리를 파악할 겸 사전 코딩을 미리 진행하고, 이와 같은 기능을 그대로 Python으로 구현했다. 

**본 랜섬웨어는 오직 학습용이며, 다른 용도로는 사용되지 않습니다.**



## Installation

Python

```sh
pip install -r requirements.txt
```

C

```sh
Do not anything
```



## Usage example

암호화 / 복호화 를 진행하기전에 암호화 대상의 경로를 필수로 두 파일의 main함수에서 지정해주어야 합니다.  

```python
target_local = "<Target_path>"
```



암호화 대상 확장자를 Custom 할 수 있습니다.

```python
if Extension in ['.hwp', '.txt']:
# or
if Extension not in ['.hwp', 'txt'] # 권장하지 않음.
```



## Release

* 0.0.1
  * Work in progress



## Meta

🙋🏻‍♂️ Name: 837477

📧 E-mail: 8374770@gmail.com

🐱 Github: https://github.com/837477

📔 Blog: https://837477.github.io



## Contributing

1. Fork it (<https://github.com/837477/ransomware_study>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request