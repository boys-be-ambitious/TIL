from tkinter import *
from tkinter import ttk
from datetime import datetime

class GUIT():
	## 생성자 ... 클래스 변수를 만들면 자동으로 실행
	def __init__(self):
		## 클래스 안에 tkhandler라는 변수를 생성
		self.tkhandler = Tk()

		## 프로그램 크기 지정
		self.tkhandler.geometry('500x500')

		## 프로그램 이름 지정
		self.tkhandler.title("Data Collection & Preprocess Automation Program")

		## label 클래스 생성
		## 추가할 창과 출력할 문자열 넣음
		## 추가할 위치를 지정하는 함수로, 아무 값을 안 넣은 경우 줄 단위로 들어감
		# self.label_title = Label(self.tkhandler, text="")
		# self.label_title.pack()

		## '종류 텍스트' 추가
		self.label_kind = Label_kind = Label(self.tkhandler, text="실거래가 구분", height=1, pady=10)
		self.label_kind.pack()

		## '콤보박스' 추가
		# https://stackoverflow.com/questions/6876518/set-a-default-value-for-a-ttk-combobox
		self.box_value = StringVar()

		self.box_value.trace("w", self.on_field_change)
		self.box = ttk.Combobox(self.tkhandler, width=40, height=1, textvariable=self.box_value, state="readonly")
		self.box["values"] = ("아파트 (매매)", "아파트 (전월세)", "오피스텔 (매매)", "오피스텔 (전월세)", "연립다세대 (매매)", "연립다세대 (전월세)")
		self.box.current(0)
		self.box.pack()

		## '년, 월' 텍스트 추가
		## 특정 형태의 조건이 아닐 경우에 에러 메시지 팝업을 뜨게 하려면?
		self.label_ym = Label(self.tkhandler, text="수집일자 입력", pady=10)
		self.label_ym.pack()
		
		## '년월' 을 입력할 수 있는 텍스트 박스 추가
		# relief는 텍스트 박스 디자인을 의미
		# 다른 값은 일부 환경에서 눈에 안 보이는 경우가 있음 (가독성)
		# bd는 테두리 두께
		self.text_params = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
		self.text_params.insert(END, "ex) 2019년 1월 -> 201901 기입")

		# 입력 창에서 엔터를 칠 경우 여러 줄 입력하게 되는 경우 방지 (ignore_enter 함수를 만든 다음에 작성)
		# 꺽쇠는 예약서, Key를 입력하는 곳에 binding을 하겠다.
		# 엔터를 치면 브레이크가 떨어져서 값이 입력되지 않음.
		self.text_params.bind("<Key>", self.ignore_enter)
		self.text_params.bind("<Return>", self.ignore_enter)
		self.text_params.bind("<Escape>", self.press_key)
		self.text_params.bind("<Tab>", self.focus_next_widget)
		self.text_params.pack()

		## '수집 시작' 버튼
		# width의 경우 실제로 값을 변경하면서 확인해야함
		# geometry에서 설정한 값과 절대값이 다름
		# auto_scraping 함수를 만들고 연결하기(command=self.auto_scraping)
		self.btn_start = Button(self.tkhandler, text = 'Activate', width=30, font=("Helvetica", 13), command=self.auto_scraping)
		self.btn_start.pack()

		## '수집 중지' 버튼을 추가
		self.btn_end = Button(self.tkhandler, text="Disabled", fg="red", width=30, font=("Helvetica", 13), command=self.auto_quit)
		self.btn_end.pack()

		## '텔레그램 ID' 입력 텍스트 박스 추가
		self.label_telegram = Label(self.tkhandler, text='Telegram ID')
		self.label_telegram.pack()

		self.text_telegram = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
		self.text_telegram.insert(END, "769375336")
		self.text_telegram.bind("<Key>", self.ignore_enter)
		self.text_telegram.bind("<Return>", self.ignore_enter)
		self.text_telegram.bind("<Escape>", self.press_key)
		self.text_telegram.bind("<Tab>", self.focus_next_widget)
		self.text_telegram.pack()

		## '텔레그램 보내기'버튼 추가
		# auto_telegram.py를 불러와서 함수로 지정하고 연결(command=self.auto_telegram)
		self.btn_telegram = Button(self.tkhandler, text="Send Telegram", width=30, command=self.auto_telegram)
		# self.btn_telegram = Button(self.tkhandler, text="Send Telegram", width=30)
		self.btn_telegram.pack()

		## '이메일 주소' 입력 텍스트 박스 추가
		self.label_email = Label(self.tkhandler, text = 'E-mail ID')
		self.label_email.pack()

		self.text_email = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
		self.text_email.insert(END, "datablocklab@gmail.com")
		self.text_email.bind("<Key>", self.ignore_enter)
		self.text_email.bind("<Return>", self.ignore_enter)
		self.text_email.bind("<Escape>", self.press_key)
		self.text_email.bind("<Tab>", self.focus_next_widget)
		self.text_email.pack()

		## '이메일 보내기'버튼 추가
		# auto_email.py를 불러와서 함수로 지정하고 연결 (command=self.auto_email)
		self.btn_email = Button(self.tkhandler, text="Send E-mail", width=30, command=self.auto_email)
		self.btn_email.pack()

		## 세로 스크롤바 생성
		# 세로 스크롤바를 생성하기 위해 orient를 vertical로 지정
		self.scroll = Scrollbar(self.tkhandler, orient='vertical')

		## 리스트 박스 생성 <-> 스크롤바와 연동
		# 리스트 박스를 생성하고, 세로 스크롤을 위에 생성한 스크롤바로 지정
		# 리스트 박스를 움직일 때, 세로 스크롤이 같이 움직이도록 설정
		self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)

		# 스크롤바의 이동 <-> 리스트 박스의 세로와 연동
		# 스크롤바를 움직일 때, 리스트 박스가 세로로 움직이도록 설정
		self.scroll.config(command=self.lbox.yview)

		# 스크롤바는 오른쪽에 붙이고 세로를 채움
		self.scroll.pack(side='right', fill='y')
		# 리스트 박스는 왼쪽에 붙이고 양쪽으로 채움
		self.lbox.pack(side='left', fill='both', expand=True)
		self.append_log('Start Program...')


	def press_key(self, event):
		# 키를 입력하면 가이드 글('ex)2019년 1월 -> 201901')이 사라지고, 입력되는 것
		if event.keysym == "Escape":
			self.text_params.delete('1.0', END)
			return 'break'

	def ignore_enter(self, event):
		# Enter 키를 치면 아무 것도 안 하겠다는 뜻
		if event.keysym == "Return":
			return 'break'

	def focus_next_widget(self, event):
		# Tab 키를 누르면 다음 위젯으로 넘어가겠다는 뜻
		if event.keysym == 'Tab':
			event.widget.tk_focusNext().focus()
			return 'break'

	# def return_key(self, event):
	# 	# enter 키를 누르면 실행하겠다는 뜻 ... space bar 도 좋음
	# 	if event.keysym == 'Return':
	# 		self.btn_start.click()
	# 		return 'break'

	# def ignore_pattern(self, event):
	# 	# 형식에 어긋나는 값을 입력하면 입력값이 올바르지 않다는 값(팝업창)이 출력

	
	def on_field_change(self, index, value, op):
		# 실거래가 구분이 바뀔 때마다 출력
		# ex) combobox updated to 아파트 (매매)
		print("Combobox updated to ", self.box.get())
		self.append_log(self.box.get())

	def auto_scraping(self):
		self.append_log('Start Data Collecting... Please Wait.')
		# from dart import get_dart_link, get_dart_info
		# from dart import get_dart_link
		# pages = self.text_params.get('1.0', END).strip()
		# get_dart_link(pages)
		# get_dart_info()

		from trade_apt import download_trade_apt
		from trade_officetel import download_trade_officetel
		from trade_rh import download_trade_rh
		from rent_apt import download_rent_apt
		from rent_officetel import download_rent_officetel
		from rent_rh import download_rent_rh
		# from trade_multifamily import download_trade_multifamily
		# from rent_multifamily import download_rent_multifamily
		## 여러 개 셀 선택해서 하나만 입력해도 선택한 여러 셀이 동일하게 입력되는 방법은?
		
		# 원하는 결과를 가져옴
		recv = self.text_params.get("1.0", END).strip()
		today = str(datetime.now())[:10]

		if self.box.get() == '아파트 (매매)':
			res = download_trade_apt(recv, guit=self)
			res.to_excel('../output/apt_trade({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/apt_trade({0}_{1}).xlsx'.format(recv, today)
		elif self.box.get() == '아파트 (전월세)':
			res = download_rent_apt(recv, guit=self)
			res.to_excel('../output/apt_rent({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/apt_rent({0}_{1}).xlsx'.format(recv, today)
		elif self.box.get() == '오피스텔 (매매)':
			res = download_trade_officetel(recv, guit=self)
			res.to_excel('../output/officetel_trade({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/officetel_trade({0}_{1}).xlsx'.format(recv, today)
		elif self.box.get() == '오피스텔 (전월세)':
			res = download_rent_officetel(recv, guit=self)
			res.to_excel('../output/officetel_rent({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/officetel_rent({0}_{1}).xlsx'.format(recv, today)
		elif self.box.get() == '연립다세대 (매매)':
			res = download_trade_rh(recv, guit=self)
			res.to_excel('../output/rh_trade({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/rh_trade({0}_{1}).xlsx'.format(recv, today)
		elif self.box.get() == '연립다세대 (전월세)':
			res = download_rent_rh(recv, guit=self)
			res.to_excel('../output/rh_rent({0}_{1}).xlsx'.format(recv, today), encoding='utf-8')
			self.res_file_path = '../output/rh_rent({0}_{1}).xlsx'.format(recv, today)
		else:
			pass
		# if self.box.get() == "단독다가구 (매매)":
		# 	res = download_(recv, guit=self)
		# 	res.to_excel("../../output/multifamily_house_trade({0}_{1}).xlsx".format(recv, today), index=False, encoding="utf-8")

		# if self.box.get() == "단독다가구 (전월세)":
		# 	res = download_(recv, guit=self)
		# 	res.to_excel("../../output/multifamily_house_rent({0}_{1}).xlsx".format(recv, today), index=False, encoding="utf-8")
		
	def auto_quit(self):
		self.append_log("Stop.")
		self.tkhandler.destroy()

	def auto_email(self):
		print("Send E-mail.")
		from auto_email import Email
		from datetime import datetime

		recv = self.text_email.get("1.0", END).strip()
		print(recv)

		self.append_log(recv + '에게 이메일을 발송합니다.')
		e = Email()
		today = str(datetime.now())[:10]
		e.send_mail('장석현', recv, attachment=self.res_file_path)
		self.append_log(recv+'에게 이메일을 발송했습니다.')


	def auto_telegram(self):
		print("send Telegram.")
		from auto_telegram import Telegram
		from datetime import datetime

		recv = self.text_telegram.get("1.0", END).strip()
		print(recv)

		self.append_log(recv + '에게 메시지를 전송합니다.')
		e = Telegram()
		today = str(datetime.now())[:10]
		e.send_telegram('장석현', recv, attachment=self.res_file_path)
		self.append_log(recv+'에게 메시지를 전송했습니다.')
	
	def append_log(self, msg):
		from datetime import datetime
		now = str(datetime.now())[11:-7] # hh:mm:ss

		# 마지막 줄에 내용을 추가
		self.lbox.insert(END, "[%s] %s"%(now, msg))
		# UI 업데이트
		self.lbox.update()
		# 마지막 줄을 보도록 이동
		self.lbox.see(END)

	def run(self):
		# 이벤트를 받기 위해 무한 반복문을 실행
		self.tkhandler.mainloop()

g = GUIT()
g.run()