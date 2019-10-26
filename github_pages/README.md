## 2. GitHub에 Jekyll 블로그 올리기 
로컬에서 만든 Jekyll 테마의 블로그 폴더를 올릴 것이다. 그리고 GitHub Pages로 Jekyll 블로그를 호스팅하여 http://username.github.io/ 로 접속하기까지 진행해볼 예정이다.


### 2.1. GitHub 저장소 만들기
우선 [GitHub](https://github.com/)에 가입한다. GitHub Pages로 호스팅하면 Username이 URL에 사용된다. Username은 바꿀 수 있지만 그래도 URL에 사용될 것을 고려해서 정하자.
로그인한 후에 `New Repository`을 누른다. Repository 이름은 `username.github.io`로 적어야한다. 그래야 GitHub Pages로 호스팅할 수 있다(~~나중에 수정할 수 있지만 이왕이면 처음부터 제대로 하자~~).
README.md는 만든 저장소의 설명서라고 생각하면 쉽다(설명 : 사용법, Copyright 등을 적는 Markdown 형식의 파일이다).


<span style="color:#FE2E64"><b>Git을 잘 모른다면... 공부할 수 있도록 내용을 정리해두었다. [해당 페이지로 이동하기](https://github.com/boys-be-ambitious/TIL/tree/master/git) </b></span>

로컬에서 폴더를 하나 생성한 다음에, 아래의 명령어를 순차적으로 실행해주면 된다(~~잘 모르겠다면 아래에 스크린샷을 참고하자~~).

<span style="color:#FE2E64"><b>boys-be-ambitious는 본인의 username이다. 각자의 username으로 넣어야 한다(꼭).</b></span>

    echo "# boys-be-ambitious.github.io" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/boys-be-ambitious/boys-be-ambitious.github.io.git
    git push -u origin master


<img src = "../images/github_pages_2_.png">
<img src = "../images/github_pages_3.png">
<img src = "../images/github_pages_4_.png">
<img src = "../images/github_pages_6.png">
<img src = "../images/github_pages_7_.png">
<img src = "../images/github_pages_8__.png">
<img src = "../images/github_pages_9_.png">
<img src = "../images/github_pages_10_.png">
<span style="color:#FE2E64"><b>2단계까지 완성되면 위의 이미지와 같은 모습을 볼 수 있다.</b></span>