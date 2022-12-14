# 사용자로부터 2개의 원에 대한 정보를 받아서 화면에 원을 그린 후에 조건문을 사용하여 큰 원 안에 작은 원이 포함되는 프로그램을 작성하라.
import turtle  # turtle 라이브러리를 불러온다.
t = turtle.Turtle()  # 변수 t를 turtle.Turtle()로 선언
t.shape("turtle")  # turtle 도형 불러오기

x1 = int(input("큰 원의 중심좌표 x1:"))  # 사용자로부터 x1 값을 받음
y1 = int(input("큰 원의 중심좌표 y1:"))  # 사용자로부터 y1 값을 받음
r1 = int(input("큰 원의 반지름:"))  # 사용자로부터 r1 값을 받음
x2 = int(input("작은 원의 중심좌표 x2:"))  # 사용자로부터 x2 값을 받음
y2 = int(input("작은 원의 중심좌표 y2:"))  # 사용자로부터 y2 값을 받음
r2 = int(input("작은 원의 반지름:"))  # 사용자로부터 r2 값을 받음

t.penup()  # 그리기 모드 시작
t.goto(x1, y1)  # (x1,y1)점으로 이동
t.pendown()  # 그리기 모드를 끝냄
t.circle(r1)  # 반지름이 r1인 원을 그림

t.penup()  # 그리기 모드 시작
t.goto(x2, y2)  # (x2,y2)점으로 이동
t.pendown()  # 그리기 모드를 끝냄
t.circle(r2)  # 반지름이 r2인 원을 그림

dist = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5  # 변수 dist에 계산식을 저장
if dist <= r1-r2:  # dist값이 r1-r2 이하이면
    # 참일시 두번째 원이 첫번째 원의 내부에 있습니다.를 출력, 거짓일시 다음 조건문으로 이동
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
elif dist <= r1+r2:  # dist값이 r1+r2 이하이면
    t.write("두번째 원이 첫번째 원과 겹칩니다.")  # 참일시 두번째 원이 첫번째 원과 겹칩니다.를 출력
else:
    turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.")  # 거짓일시 두번째 원이 첫번째 원과 겹치지 않습니다.를 출력
t.screen.exitonclick()  # 화면을 마우스로 클릭해야 종료됨
