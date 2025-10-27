import turtle
import time
import random

delay = 0.1
score = 0
game_over = False

# --- تنظیم صفحه ---
screen = turtle.Screen()
screen.title("🐍 Snake Game with Background & Game Over")
screen.setup(width=700, height=600)
screen.tracer(0)

# پس‌زمینه (GIF باید در همان فولدر باشد)
try:
    screen.bgpic("ezgif.com-animated-gif-maker.gif")
except:
    screen.bgcolor("lightgreen")

# --- سر مار ---
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

# --- غذا ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# --- نمایش امتیاز ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 24, "bold"))

# --- پیام Game Over ---
over_text = turtle.Turtle()
over_text.hideturtle()
over_text.color("red")
over_text.penup()
over_text.goto(0, 0)

# --- توابع حرکت ---
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# --- کنترل‌ها ---
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- حلقه‌ی اصلی ---
while True:
    screen.update()

    # اگر Game Over شده، متوقف شو
    if game_over:
        time.sleep(2)
        break

    # برخورد با دیواره‌ها (سوزش و Game Over)
    if (
        head.xcor() > 340 or head.xcor() < -340 or
        head.ycor() > 280 or head.ycor() < -280
    ):
        head.color("red")
        over_text.write("🔥 GAME OVER 🔥", align="center", font=("Arial", 36, "bold"))
        game_over = True
        continue

    # برخورد با غذا
    if head.distance(food) < 20:
        # انتقال تصادفی غذا
        x = random.randint(-320, 320)
        y = random.randint(-260, 260)
        food.goto(x, y)

        # افزودن قطعه جدید
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()
        segments.append(new_segment)

        # افزایش امتیاز
        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    # حرکت بدن
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # بخش اول بدن به موقعیت سر بره
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # بررسی برخورد با خودش
    for segment in segments:
        if segment.distance(head) < 20:
            head.color("red")
            over_text.write("💀 GAME OVER 💀", align="center", font=("Arial", 36, "bold"))
            game_over = True
            break

    time.sleep(delay)

turtle.done()
