# 텍스트 메일 전송시 필요한 클래스
from email.mime.text import MIMEText
# SMTP에서 사용하는 규약에 맞춰서 내용을 작성해주는 클래스
from email.mime.multipart import MIMEMultipart
# SMTP로 메일을 전송하기 위한 라이브러리
import smtplib

# SMTP 접속을 위한 서버 주소
SMTP_SERVER='smtp.gmail.com'
# SMTP 접속을 위한 서버의 포트 번호
SMTP_PORT=465
# 계정 정보 (gmail만 가능)
SMTP_USER='datablocklab@gmail.com'
SMTP_PASSWORD=''

class Email():
	subj_layout = '님에게 메일 도착'
	cont_layout = '''님에게 메일이 도착하였습니다.
안녕하세요? 자동화로 보내지는 메일입니다.
하루하루는 성실하게, 인생전체는 되는대로.
'''

	def is_valid_email(self, addr):
		import re
		if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
			return True
		else:
			return False

	def send_mail(self, name, addr, cc='', hidden_cc='', contents='', attachment=None):
		# SMTP로 보내기 위한 기본 형태를 가진 클래스 변수 생성
		msg = MIMEMultipart('alternative')

		# 첨부파일이 있는 경우에 mixed로 Multipart 생성
		if attachment:
			msg = MIMEMultipart('mixed')

		# 보내는 사람, 받는사람, 제목을 추가
		msg['From'] = SMTP_USER
		msg['To'] = addr
		msg['CC'] = cc
		msg['Subject'] = name + self.subj_layout

		if not contents:
			contents = name + self.cont_layout
		#text = MIMEText(contents)
		# html로 보내고자 할때 사용
		text = MIMEText(contents) 
		msg.attach(text)

		# 첨부파일이 있을 경우에 이를 추가하기 위한 코드 수행
		if attachment:
			# 파일 데이터를 추가하기 위한 클래스
			from email.mime.base import MIMEBase
			# 파일을 전송 가능한 형태로 변경하기 위한 클래스
			from email import encoders

			# 빈 MIMEBase 클래스 변수 생성
			# octect-stream은 모든 일반파일을 의미
			file_data = MIMEBase('application', 'octect-stream')
			# 입력받은 파일명으로 파일을 open하고, 해당 데이터를 위 클래스 변수에 넣음
			data = open(attachment, 'rb').read()
			file_data.set_payload(data)
			# 전송가능한 base64 형태로 변환
			encoders.encode_base64(file_data)

			# 파일명을 직접 명시해야하기 때문에 파일경로로부터 파일명만 가져옴
			import os
			filename = os.path.basename(attachment)
			# 파일명 정보를 추가
			file_data.add_header('Content-Disposition', 'attachment; filename="'+filename+'"')
			# 파일 데이터를 Multipart에 추가
			msg.attach(file_data)

		# 서버와 통신하기 위한 클래스 변수인 smtp를 생성
		smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
		# SMTP 서버에 로그인
		smtp.login(SMTP_USER, SMTP_PASSWORD)

		# 모든 수신 대상자를 콤마로 연결
		targets = ','.join((addr,cc,hidden_cc))
		# 메일 전송 (모든 대상자를 리스트형태로 만들어서 발송)
		smtp.sendmail(SMTP_USER, targets.split(','), msg.as_string())
		# 닫기
		smtp.close()


if __name__ == '__main__':
	e = Email()
	e.send_mail('장석현', 'jangsh1112@gmail.com,naraaction@naver.com',      # 받는사람
		'datablocklab@gmail.com,savetheearth1112@gmail.com',             # 참조
		'datadatelab@gmail.com')                     




















