

```python
import numpy as np
import pandas as pd
import plotly as plt
import plotnine as p9
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())
%matplotlib inline
```


```python
hos = pd.read_excel("../../Downloads/localdata/hospital.xlsx")
cli = pd.read_excel("../../Downloads/localdata/clinic.xlsx")
pha = pd.read_excel("../../Downloads/localdata/pharmacy.xlsx")
pcw = pd.read_excel("../../Downloads/localdata/postpartum_care_worker.xlsx")
```


```python
elements = [hos, cli, pha, pcw]

[el.shape for el in elements]

for el in elements:
    print(el.shape)
    print(el['영업상태명'].value_counts())
    print(el.columns)
    print("=" * 100)
```

    (5774, 44)
    영업/정상             3863
    폐업                1720
    취소/말소/만료/정지/중지     118
    휴업                  73
    Name: 영업상태명, dtype: int64
    Index(['번호', '개방서비스명', '개방서비스ID', '개방자치단체코드', '관리번호', '인허가일자', '인허가취소일자',
           '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명', '폐업일자', '휴업시작일자', '휴업종료일자',
           '재개업일자', '소재지전화', '소재지면적', '소재지우편번호', '소재지전체주소', '도로명전체주소', '도로명우편번호',
           '사업장명', '최종수정시점', '데이터갱신구분', '데이터갱신일자', '업태구분명', '좌표정보(X)', '좌표정보(Y)',
           '의료기관종별명', '의료인수', '입원실수', '병상수', '총면적', '진료과목내용', '진료과목내용명', '지정취소일자',
           '완화의료지정형태', '완화의료담당부서명', '구급차특수', '구급차일반', '총인원', '구조사수', '허가병상수',
           '최초지정일자'],
          dtype='object')
    ====================================================================================================
    (103383, 44)
    영업/정상             67139
    폐업                35714
    취소/말소/만료/정지/중지      388
    휴업                  142
    Name: 영업상태명, dtype: int64
    Index(['번호', '개방서비스명', '개방서비스ID', '개방자치단체코드', '관리번호', '인허가일자', '인허가취소일자',
           '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명', '폐업일자', '휴업시작일자', '휴업종료일자',
           '재개업일자', '소재지전화', '소재지면적', '소재지우편번호', '소재지전체주소', '도로명전체주소', '도로명우편번호',
           '사업장명', '최종수정시점', '데이터갱신구분', '데이터갱신일자', '업태구분명', '좌표정보(X)', '좌표정보(Y)',
           '의료기관종별명', '의료인수', '입원실수', '병상수', '총면적', '진료과목내용', '진료과목내용명', '지정취소일자',
           '완화의료지정형태', '완화의료담당부서명', '구급차특수', '구급차일반', '총인원', '구조사수', '허가병상수',
           '최초지정일자'],
          dtype='object')
    ====================================================================================================
    (60026, 30)
    폐업                37258
    영업/정상             22577
    취소/말소/만료/정지/중지      154
    휴업                   37
    Name: 영업상태명, dtype: int64
    Index(['번호', '개방서비스명', '개방서비스ID', '개방자치단체코드', '관리번호', '인허가일자', '인허가취소일자',
           '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명', '폐업일자', '휴업시작일자', '휴업종료일자',
           '재개업일자', '소재지전화', '소재지면적', '소재지우편번호', '소재지전체주소', '도로명전체주소', '도로명우편번호',
           '사업장명', '최종수정시점', '데이터갱신구분', '데이터갱신일자', '업태구분명', '좌표정보(X)', '좌표정보(Y)',
           '약국영업면적', '지정일자'],
          dtype='object')
    ====================================================================================================
    (904, 47)
    영업/정상             564
    폐업                316
    휴업                 23
    취소/말소/만료/정지/중지      1
    Name: 영업상태명, dtype: int64
    Index(['번호', '개방서비스명', '개방서비스ID', '개방자치단체코드', '관리번호', '인허가일자', '인허가취소일자',
           '영업상태구분코드', '영업상태명', '상세영업상태코드', '상세영업상태명', '폐업일자', '휴업시작일자', '휴업종료일자',
           '재개업일자', '소재지전화', '소재지면적', '소재지우편번호', '소재지전체주소', '도로명전체주소', '도로명우편번호',
           '사업장명', '최종수정시점', '데이터갱신구분', '데이터갱신일자', '업태구분명', '좌표정보(X)', '좌표정보(Y)',
           '임산부정원수', '영유아정원수', '임산부실면적', '영유아실면적', '모유수유실면적', '급식시설면적', '세탁실면적',
           '목욕실면적', '조리원화장실면적', '사무실면적', '간호사수', '간호조무사수', '영양사수', '취사부수', '미화원수',
           '기타인원수', '건물층수', '지상층수', '지하층수'],
          dtype='object')
    ====================================================================================================


### 영업 상태 현황 1 : 병원


```python
pysqldf("select \
    영업상태명 \
    , freq \
    , round(100. * freq/tot_freq, 1) as prob \
from ( \
    select \
        영업상태명 \
        , count(*) as freq \
    from hos \
    group by 영업상태명 \
    ) as a, ( \
    select \
        count(*) as tot_freq \
    from hos \
    ) as b;")
    
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>영업상태명</th>
      <th>freq</th>
      <th>prob</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영업/정상</td>
      <td>3863</td>
      <td>66.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>취소/말소/만료/정지/중지</td>
      <td>118</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>폐업</td>
      <td>1720</td>
      <td>29.8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>휴업</td>
      <td>73</td>
      <td>1.3</td>
    </tr>
  </tbody>
</table>
</div>



### 영업 상태 현황 2 : 의원


```python
pysqldf("select \
    영업상태명 \
    , freq \
    , round(100. * freq/tot_freq, 1) as prob \
from ( \
    select \
        영업상태명 \
        , count(*) as freq \
    from cli \
    group by 영업상태명 \
    ) as a, ( \
    select \
        count(*) as tot_freq \
    from cli \
    ) as b;")
    
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>영업상태명</th>
      <th>freq</th>
      <th>prob</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영업/정상</td>
      <td>67139</td>
      <td>64.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>취소/말소/만료/정지/중지</td>
      <td>388</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>폐업</td>
      <td>35714</td>
      <td>34.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>휴업</td>
      <td>142</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>
</div>



### 영업 상태 현황 3 : 약국


```python
pysqldf("select \
    영업상태명 \
    , freq\
    , round(100. * freq/tot_freq, 1) as prob \
from ( \
    select \
        영업상태명 \
        , count(*) as freq \
    from pha \
    group by 영업상태명 \
    ) as a, ( \
    select \
        count(*) as tot_freq \
    from pha \
    ) as b;")

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>영업상태명</th>
      <th>freq</th>
      <th>prob</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영업/정상</td>
      <td>22577</td>
      <td>37.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>취소/말소/만료/정지/중지</td>
      <td>154</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>폐업</td>
      <td>37258</td>
      <td>62.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>휴업</td>
      <td>37</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>
</div>



### 영업 상태 현황 4 : 산후조리원


```python
pysqldf("select \
    영업상태명 \
    , freq \
    , round(100. * freq/tot_freq, 1) as prob \
from ( \
    select \
        영업상태명 \
        , count(*) as freq \
    from pcw \
    group by 영업상태명 \
    ) as a, ( \
    select \
        count(*) as tot_freq \
    from pcw \
    ) as b;")
    
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>영업상태명</th>
      <th>freq</th>
      <th>prob</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>영업/정상</td>
      <td>564</td>
      <td>62.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>취소/말소/만료/정지/중지</td>
      <td>1</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>폐업</td>
      <td>316</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>휴업</td>
      <td>23</td>
      <td>2.5</td>
    </tr>
  </tbody>
</table>
</div>



## Summary 1
- 병원 : 전체 5,744개의 병원 중 정상 영업중인 병원은 3,863개 (67.3%), 폐업한 병원은 1,720개 (29.9%)
- 의원 : 전체 103,383개의 의원 중 정상 영업중인 병원은 67,139개 (64.9%), 폐업한 병원은 35,714개 (34.5%)
- 약국 : 전체 60,026개의 약국 중 정상 영업중인 약국은 22,577개 (37.6%), 폐업한 약국은 37,258개 (62.1%)
- 산후조리원 : 전체 904개의 산후조리원 중 정상 영업중인 조리원은 564개 (62.4%), 폐업한 조리원은 316개 (35%)

1. 업종별, 지역별 영업상태 현황 파악
2. 지역별 업종 및 영업상태 현황 파악
---
1. SQL Report (ratio) ... 업종별 현황 ... 시계열로 들어와서 일자별로 트레킹이 가능하다면 추이도 파악하고 싶음
2. 평균 영업 기간 (영업중인 영업점, 폐업한 영업점, 휴업한 영업접)
3. 지역별 현황
4. 지역별 업종별 현황
5. 지도 시각화
6. 시각화
