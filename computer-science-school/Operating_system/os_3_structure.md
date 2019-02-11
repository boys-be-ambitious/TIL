# Operating System Structure
### [Back to OS Home](https://github.com/boys-be-ambitious/TIL/tree/master/computer-science-school/Operating_system)
---

![os_structure](../../images/os_str_1.jpg)
[![HitCount](http://hits.dwyl.io/boys-be-ambitious//Operating_system/os_3_structure.md.svg)](http://hits.dwyl.io/boys-be-ambitious//Operating_system/os_3_structure.md)


# 1. System Call

## 1.1. 응용프로그램, 운영체제, 컴퓨터 하드웨어(시스템 리소스) 관계
### 도서관에 비유
    - 운영체제 : 도서관
    - 응용 프로그램 : 시민
    - 컴퓨터 하드웨어 : 책
    - 운영체제의 역할
        - 시민은 도서관에 원하는 책(자원)을 요청
        - 도서관은 적절한 책을 찾아서, 시민에게 대여
        - 시민의 기한이 다 되면, 도서관이 해당 책(자원) 회수

<center><img src="../../images/os_7.png"></center>

> 출처 : 구글

- 운영체제는 응용 프로그램이 요청하는 메모리를 허가하고, 분배한다.
- 운영체제는 응용 프로그램이 요청하는 CPU 시간을 제공한다.
- 운영체제는 응용 프로그램이 요청하는 IO Devices 사용을 허가/제어한다.

## 1.2. 운영체제는 사용자 인터페이스 제공
    - 쉘 (Shell)
        - 사용자가 운영체제 기능과 서비스를 조작할 수 있도록 인터페이스를 제공하는 프로그램
        - 쉘은 터미널 환경(CLI)과 GUI 환경 두 종류로 분류

## 1.3. 운영체제는 응용 프로그램을 위해서도 인터페이스를 제공
    - API (Application Programming Interface)
        - 함수로 제공
        - open()
    - 보통은 라이브러리(library) 형태로 제공
        - C library
        - https://www.gnu.org/software/libc/

- 운영체제는 사용자 뿐만 아니라, 응용 프로그램을 위해서도 인터페이스를 제공해준다.
- 사용자 인터페이스를 제공해주기 위해 별도의 shell 프로그램을 제공한다.
- OS 바로 전 단계에 (함수의 집합, 요청서의 집합인) API가 있다.
- 운영체제가 제공해주는 API를 가지고 Shell(도 하나의 응용 프로그램이니까)이라는 프로그램을 만든다. 
- Application도 운영체제의 특별한 기능을 쓰고 싶을 때에는 API를 사용해야한다.


## 1.4. System Call
    - 시스템 콜 또는 시스템 호출 인터페이스
    - 운영체제가 운영체제 각 기능을 (응용 프로그램에서) 사용할 수 있도록 시스템 콜이라는 명령 또는 함수를 제공
    - API 내부에는 (해당 운영체제 기능을 사용할 수 있는)시스템콜을 호출하는 형태로 만들어지는 경우가 대부분


<center><img src="../../images/systemcall_1.gif"></center>

> 출처 : 구글

## 1.5. 운영체제를 만든다면?
    1. 운영체제 개발 (핵심 운영체제 software - Kernel)
    2. 시스템 콜 개발
    3. C API(library) 개발
    4. (사용자를 위한) shell 프로그램 개발
    5. 응용 프로그램 개발

## 1.5. 운영체제와 시스템 콜
- 표준 시스템 콜 정의
- [POSIX API](https://docs.oracle.com/cd/E19048-01/chorus4/806-3328/6jcg1bm05/index.html), Windows API

> - API(library) : 각 언어별 운영체제 기능 호출 인터페이스 함수 (각 언어별 인터페이스)
> - 시스템 콜 : 운영체제 기능을 호출하는 함수


## Summary
    - 운영체제는 컴퓨터 하드웨어와 응용 프로그램을 관리한다.
    - 사용자 인터페이스를 제공하기 위해 쉘 프로그램을 제공한다.
    - 응용 프로그램이 운영체제 기능을 요청하기 위해서, 운영체제는 시스템 콜을 제공한다.
        - 보통 시스템 콜을 직접 사용하기 보다는, 해당 시스템 콜을 사용해서 만든 각 언어별 라이브러리(API)를 사용한다.