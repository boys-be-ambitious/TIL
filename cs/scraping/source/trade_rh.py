## 1. 라이브러리 호출

import requests
from lxml.ElementInclude import urlopen
import xml.etree.ElementTree as etree
from bs4 import BeautifulSoup
import pandas as pd

from rt_setting import Rt_Setting
# from setting import Bjd_Ym_Setting
# setting = Bjd_Ym_Setting()
setting = Rt_Setting()
year_month = setting.year_month()
ym_list = setting.year_month_list()
LAWD_CD = setting.lawd_cd()
sigungu_dict = setting.sigungu_dict()


## 2. 스크래핑 함수
def get_rh_trade_data (loc, ym):
	key = "U01n1ERAP3rooP6xztJBrjzTM95nrzASy%2Bw%2BHZRXCmH1ZYON516m6alV%2F%2BUKNfUtvREtal7DVAX0ZU5ltW2xrg%3D%3D" #인증키
	url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?LAWD_CD=" + str(loc) + "&DEAL_YMD=" + str(ym) + "&serviceKey=" + key
	resp = urlopen()
	xml = resp.read().decode('UTF-8')	 # 데이터를 가져오고 UTF-8 String으로 변환
	
	root = etree.fromstring(xml)
	result = []
	

	for child in root.iter("item"):
		trade_amount = child.findtext('거래금액')
		year_of_construction = child.findtext('건축년도')
		year = child.findtext('년')
		site_right_area = child.findtext('대지권면적')
		dong = child.findtext('법정동')
		house_type = child.findtext('연립다세대')
		month = child.findtext('월')
		day = child.findtext('일')
		exclusive_private_area = child.findtext('전용면적')
		jibun = child.findtext('지번')
		area_code = child.findtext('지역코드')
		floor = child.findtext('층')

		
		rent_or_keyrent = rent.replace(",", "")
		
		 # 본번, 부번 세팅
		if jibun is not None and '산' not in jibun and '-' not in jibun:
			if len(jibun) == 1:
				bon = '000' + jibun
				bu = '0000'
			elif len(jibun) == 2:
				bon = '00' + jibun
				bu = '0000'
			elif len(jibun) == 3:
				bon = '0' + jibun
				bu = '0000'
			elif len(jibun) == 4:
				bon = jibun
				bu = '0000'
		elif jibun is not None and '산' not in jibun and '가' not in jibun and 'B' not in jibun and '-' in jibun:
			if jibun[1] == '-':
				if len(jibun) == 3:
					bon = '000' + jibun[0]
					bu = '000' + jibun[2]
				elif len(jibun) == 4:
					bon = '000' + jibun[0]
					bu = '00' + jibun[2:]
				elif len(jibun) == 5:
					bon = '000' + jibun[0]
					bu = str(0) + jibun[2:]
				else:
					bon = '000' + jibun[0]
					bu = jibun[2:] 
			elif jibun[2] == '-':
				if len(jibun) == 4:
					bon = '00' + jibun[0:2]
					bu = '000' + jibun[3]
				elif len(jibun) == 5:
					bon = '00' + jibun[0:2]
					bu = '00' + jibun[3:]
				elif len(jibun) == 6:
					bon = '00' + jibun[0:2]
					bu = '0' + jibun[3:]
				else:
					bon = '00' + jibun[0:2]
					bu = jibun[3:]
			elif jibun[3] == '-':
				if len(jibun) == 5:
					bon = '0' + jibun[0:3]
					bu = '000' + jibun[4]
				elif len(jibun) == 6:
					bon = '0' + jibun[0:3]
					bu = '00' + jibun[4:]
				elif len(jibun) == 7:
					bon = '0' + jibun[0:3]
					bu = '0' + jibun[4:]
				else:
					bon = '0' + jibun[0:3]
					bu = jibun[4:]
			elif jibun[4] == '-':
				if len(jibun) == 6:
					bon =  jibun[0:4]
					bu = '000' + jibun[5]
				elif len(jibun) == 7:
					bon =  jibun[0:4]
					bu = '00' + jibun[5:]
				elif len(jibun) == 8:
					bon =  jibun[0:4]
					bu = '0' + jibun[5:]
				else:
					bon =  jibun[0:4]
					bu = jibun[5:]
		# 번지에 산이 들어간 경우
		elif jibun is not None and jibun[0] == '산':
				if len(jibun) == 7:		 
					if jibun[4] == '-':	  # 산147-23
						bon = '0' + jibun[1:4]
						bu = '00' + jibun[5:]
					elif jibun[3] == '-':	## 산23-147
						bon = '00' + jibun[1:3]
						bu = '0' + jibun[4:]
				elif len(jibun) == 6:	   
					if jibun[4] == '-':	 # 산149-3 
						bon = '0' + jibun[1:4]
						bu = '000' + jibun[5]
					elif jibun[3] == '-':   # 산74-10
						bon = '00' + jibun[1:3]
						bu = '00' + jibun[4:]
					elif jibun[2] == '-':  ## 산3-149
						bon = '000' + jibun[1]
						bu = '0' + jibun[3:]
				elif len(jibun) == 5:
					if jibun[3] == '-':	 # 산56-1
						bon = '00' + jibun[1:3]
						bu = '000' + jibun[4:]
					elif jibun[2] == '-':	## 산5-10
						bon = '000' + jibun[1]
						bu = '00' + jibun[3:]
				elif len(jibun) == 4:
					if jibun in '-':		# 산2-9
						bon = '000' + jibun[1:2]
						bu = '000' + jibun[3]
					elif jibun not in '-':  # 산103
						bon = '0' + jibun[1:]
						bu = '0000'
				elif len(jibun) == 3:	   # 산46
					if '-' not in jibun:
						bon = '00' + jibun[1:3]
						bu = '0000'
					elif '-' in jibun:	  ## 산1-1
						bon = '000' + jibun[1]
						bu = '000' + jibun[3]
		# 번지에 산이 들어간 경우
		elif jibun is not None and jibun[0] == '가':
			if len(jibun) == 2:			# 가-
				bon = '0000'
				bu = '0000'
			elif len(jibun) == 9:		  # 가-6013-15
				bon = jibun[2:6]
				bu = jibun[7:]
			elif len(jibun) == 7:		  # 가-58-36
				bon = '00' + jibun[2:4]
				bu =  '00' + jibun[5:]
			elif len(jibun) == 6:		  # 가-84-1
				bon = '00' + jibun[2:4]
				bu = '000' + jibun[5]
			elif len(jibun) == 5:
				if jibun[3] == '-':		# 가-3-1
					bon = '000' + jibun[2]
					bu = '000' + jibun[4]
				else:					  # 가-353
					bon = '0' + jibun[2:]
					bu = '0000'
			elif len(jibun) == 4:		  # 가-28
				bon = '00' + jibun[2:]
				bu = '0000'
		elif jibun is not None and jibun[0] == 'B':
			if len(jibun) == 10:		   # BL 126-1-1
				bon = '0' + jibun[3:6]
				bu = '0' + jibun[7] + '0' + jibun[9]
			elif len(jibun) == 9:		  # BL 126--1
				bon = '0' + jibun[3:6]
				bu = '000' + jibun[-1]
			elif len(jibun) == 8:		 # BL 74--2
				bon = '00' + jibun[3:5]
				bu = '000' + jibun[-1]
			elif len(jibun) == 7:			   # BL-2-10 / BL-A211 / BL-49-4
				if jibun[5] == '-':			 # BL-49-4
					bon = '00' + jibun[3:5]
					bu = '000' + jibun[-1]
				elif jibun[4] == '-':		   # BL-2-10
					bon = '000' + jibun[3]
					bu = '00'+ jibun[-2:]
				elif jibun[3] == 'A':		   # BL-A211
					bon = jibun[3:]
					bu = '0000'
			elif len(jibun) == 6:			   # BL-530 / BL-1-1
				if jibun[4] == '-':			 # BL-1-1
					bon = '000' + jibun[3]
					bu = '000' + jibun[5]
				else:						   # BL-530
					bon = '0' + jibun[3:]
					bu = '0000'	
			elif len(jibun) == 5:		# BL-A8
				bon = '00' + jibun[3:]
				bu = '0000'
			elif len(jibun) == 4:		# BL-1
				bon = '000' + jibun[-1]
				bu = '0000'
			elif len(jibun) == 3:	   # BL-
				bon = '0000'
				bu = '0000'
		else:
			bon = '0000'
			bu = '0000'
			
		# 계약년월 세팅 ... 2017 +7 => 20177 로 나와서 201707로 나오게끔 세팅해야함!
		if len(month) == 1:
			month = str(0) + month
		else:
			month = month
		trade_ym = year + month
		
		# 시군구동 세팅
		sigungu_dong = sigungu_dict[area_code] + '' + dong

		result.append({
			'시군구동': sigungu_dong,
			'번지': jibun,
			'본번': bon,
			'부번': bu,
			'건물명': house_type,
			'전용면적': exclusive_private_area,
			'대지권면적': site_right_area,
			'계약년월': trade_ym,
			'계약일': day,
			'거래금액': trade_amount,
			'층': floor,
			'건축년도': year_of_construction
		})
		
	rh_trade = pd.DataFrame(result, columns=['시군구동', '번지', '본번', '부번', '건물명', '전용면적', '대지권면적', '계약년월', '계약일', '거래금액', '층', '건축년도'])
	return(rh_trade)


## 3. 다운로드 함수 ... 하나의 년월 값만 입력 가능
def download_trade_rh(year_month, num_retries=10, guit=None):
	from urllib.error import HTTPError
	df = pd.DataFrame()
	print('Downloading: %s'%year_month)
	try:
		for i in range(len(LAWD_CD)):
			msg = 'Downloading: '+ sigungu_dict[LAWD_CD[i]]+' ('+LAWD_CD[i]+') ...'+ str(i)+'/'+str(len(LAWD_CD)-1)+'개 ...'+str(round((i/(len(LAWD_CD)-1))*100, 2))+'%'
			if guit:
				guit.append_log(msg)
			else:
				print(msg)
			get_data = get_rh_trade_data(LAWD_CD[i], year_month)
			df = df.append(get_data, ignore_index=True)
	except HTTPError as e:
		msg2 = 'Download error: '+ str(e.reason)
		if guit:
			guit.append_log(msg2)
		else:
			print(msg2)
		df = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				# 5xx HTTP 오류 시 재시도
				return download(i, num_retries - 1)
	# final msg
	final_msg = '다운로드 완료'
	if guit:
		guit.append_log(final_msg)
	else:
		print(final_msg)
	# file save
	return df