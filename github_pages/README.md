# 별것 아니지만 도움이 되는 : GitHub 블로그 (Pages) 만들기


<b> Jekyll를 설치하여, 쉽고 빠르게 나만의 Blog 만들기 </b>

포트폴리오를 정리할 겸, Github Pages를 만들어 보려고 한다. [Jekyll 공식 사이트](https://jekyllrb-ko.github.io/)에 나와 있는 빠른 시작 방법을 참고했다.


## Jekyll 설치를 위한 환경 만들기
- macOS Catalina를 기준(19.10.20)으로 작성했다.


### 1. Command Line Tools 설치하기

터미널에서 아래와 같은 명령어를 작성하여 설치한다. <br>
~~이미 설치했다면 넘어간다.~~

    # 설치
    xcode-select --install

[Xcode 홈페이지](https://developer.apple.com/xcode/)

### 2. Home Brew 설치하기
각종 커맨드라인 프로그램을 손쉽게 설치해주는 맥용 패키지 매니저로 리눅스의 apt나 yum과 비슷하다. <br>
다양한 프로그램을 복잡한 빌드과정 없이 손쉽게 설치할 수 있고 업데이트, 관리도 간단하므로 쓰지 않을 이유가 없는 필수 프로그램이다.

~~이미 설치했다면 넘어간다.~~

    # 설치
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    # 확인
    $ brew doctor
    Your system is ready to brew.

[Homebrew 홈페이지](https://brew.sh/) / [brew 명령어](https://docs.brew.sh/Manpage.html) / [brew 패키지 검색](https://formulae.brew.sh/)

### 3. Home Brew로 Ruby Version Manager rbenv 설치하기
    # rbenv 설치
    brew install rbenv ruby-build

    # ruby 설치
    rbenv install

### 4. Jekyll 설치하기
    # jekyll 설치
    sudo gem install jekyll

### 5. 로컬에 Jekyll로 블로그 만들기
    # github page 만들기
    jekyll new my-first-site


위 코드는 Jekyll에게 my-first-site라는 이름의 새 Blog를 만들어달라는 명령이다. 그러므로 my-first-site는 만들고자 하는 Blog 이름으로 대체하면 된다. 새로운 블로그를 만들지 않고 괜찮은 테마를 찾아서 Fork를 떠서 수정하는 방법도 있다(일단 새로운 블로그를 만들어보자).

위의 코드를 실행하면 로컬의 최상위 폴더에 my-first-site라는 이름의 폴더가 생성된다. 이 폴더가 나의 블로그다. 이 폴더를 Github Repository에 Push하고 Github Pages로 Publishing 하면 URL로 접근할 수도 있다.

### 6. 서버 띄어서 새로운 블로그 보기
    # 디렉토리 이동
    cd my-first-site

    # 서버 띄우기
    jekyll serve

위의 코드를 실행하면 터미널에 서버 주소(Server address: http://127.0.0.1:4000/)가 보일 것이다. 해당 주소로 접근하면 새로운 블로그를 볼 수 있다. 서버를 끄려면 `Ctrl` + `c`를 누르면 된다(`Command`가 아니고 `Ctrl`이다).


<img src = "../images/github_pages_1.png">