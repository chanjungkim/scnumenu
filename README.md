# 순천대학교 메뉴 Spring Project
2018년도 하반기 전의 구사이트에서 하루의 식단을 가져오는 프로젝트입니다.

모든 메뉴를 가져오면 좋겠지만 그렇게 하기 어렵게 규칙성 없이 사이트가 만들어진 데다가 규칙성을 맞게 관리가 되고 있어 어쩔 수 없이 수작업으로 작업을 해야하는 부분이라 그렇게 할 수 없기 때문에 하루 식단만 구현하였습니다.

## python-crawling
학교 페이지에서 메뉴 부분을 crawling하고 저장하는 소스입니다.

## spring-server
학교 페이지에서 메뉴 부분을 crawling하고 저장한 home.jsp을 보여주는 폴더입니다.

`spring-server\WEB-INF\views`에 이미 `python-crawling`폴더의 소스들이 포함되어있습니다.

2018년도 하반기에 사이트가 새로 개편하면서 url주소는 물론, html구조가 바뀌었기 때문에 crawling부분이 제대로 먹히지 않습니다. 앞으로도 바뀔 것이기 때문에 그에 맞게 쓰시면 되겠습니다.

## 실행방법
Spring 서버를 실행하신 후, python파일을 따로 background로 돌려 Scheduler를 통해 최소 하루에 한 번 crarwling을 하도록 세팅을 해주셔야합니다(새벽 5시 쯤. 사람들이 일어나기 전)

디버깅하실 때는 하루에 한 번 실행되도록 하면 디버깅 하기가 어렵기 때문에 알맞게 조정하시면 됩니다.

# License

```
Copyright 2018 Chanjung Kim

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
