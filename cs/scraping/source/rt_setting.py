## 세팅을 위한 클래스 생성
class Rt_Setting:
	## 1. lawd_cd (list)를 만들기 위한 메서드
	def lawd_cd(self):
		lines = []
		## preprocessing data 1 - txt ... append ... list
		# output: [['1111000000\t서울특별시 종로구\t존재\n'],...]
		for line in open("../input/sigungu.txt"):
			lines.append(line.split(','))

		## preprocessing data 2 - 하나의 str로 뭉쳐져 있는 list의 세 가지 속성을 구분자로 나누는 전처리
		# output: [['1111000000', '서울특별시 종로구', '존재'], ...]
		# 추후에 다른 메서드(sigungu_dict)에서 사용하기 위해 self. 지정
		self.bjd_list = []
		for line in lines:
			## preprocessing 2-1
			# line의 ','를 모두 join ... list of lists -> list
			# output: ['1111000000\t서울특별시 종로구\t존재\n', ...]
			string = ",".join(line)
			## preprocessing 2-2
			# 전처리한 string의 앞-뒤 공백 제거
			# output: ['1111000000\t서울특별시 종로구\t존재', ...]
			strip = string.strip()
			## preprocessing 2-3
			# 전처리한 strip을 구분자('\t')로 나눠서 list에 적재 ... list -> list of lists
			# output: [['1111000000', '서울특별시 종로구', '존재'], ...]
			split = strip.split('\t')
			self.bjd_list.append(split)

		## OUTPUT_1 - LAWD_CD ... ['법정동 코드', ...]
		# output: ['11110', ...]
		LAWD_CD = []
		for i in range(len(self.bjd_list)):
			# 법정동 폐지 여부가 '존재'일 경우
			if self.bjd_list[i][2] == '존재':
				# 법정동 코드 중 앞에 5자리만 추출
				bjd_code = self.bjd_list[i][0][:5]
				# 추출한 5자리 법정동 코드를 list에 추가
				LAWD_CD.append(bjd_code)
				# list 중복값 제거(set)
				LAWD_CD = list(set(LAWD_CD))

			else:
				continue
		# 중복을 제거한 list에 값을 정렬 (sorted)
		LAWD_CD = sorted(LAWD_CD)
		return LAWD_CD

	## 2. sigungu_dict (dictionary)를 만들기 위한 메서드
	def sigungu_dict(self):
		LAWD_CD = self.lawd_cd()
		sigungu_dict = {}
		for i in LAWD_CD:
			code_number = i
			code_full_number = i + ('0' * 5)
			for j in range(len(self.bjd_list)):
				if code_full_number == self.bjd_list[j][0]:
					sigungu_name = self.bjd_list[j][1]
					code_sigungu_dict = {code_number: sigungu_name}
					sigungu_dict.update(code_sigungu_dict)
				else:
					pass
		return sigungu_dict

	## 3. ym (list)를 만들기 위한 메서드
	def year_month(self):
		# 추후에 다른 메서드(year_month_list에서 활용하기 위해 self 지정
		self.ym = []
		# 2006~2017년
		for i in range(6, 19+1):
			year = str(i)
			if len(year) == 1:
				year = '200' + year
			else:
				year = '20' + year
			# 1~12월
			for j in range(1, 12+1):
				month = str(j)
				if len(month) == 1:
					month = '0' + month
				else:
					month = month
				year_month = year + month
				self.ym.append(year_month)
		return self.ym

	## 4. year_month_list (list)를 만들기 위한 메서드
	def year_month_list(self):
		# ym (list)를 사용하기 위해 메서드(year_month) 호출
		ym = self.year_month()
		self.ym_list = []
		i = 0
		while i < len(ym):
			self.ym_list.append(ym[i:i+12])
			i+=12
		return self.ym_list