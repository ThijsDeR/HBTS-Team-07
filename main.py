import tkinter as tk
from tkinter import ttk
from math import cos, sin, pi
from bluetooth import Arduino
from speechToWord import SpeechToWord

root = tk.Tk()

bluetooth = Arduino("COM3", 9600)
speechToWord = SpeechToWord()

def move_forward():
    bluetooth.send_command(bluetooth.forward)
    label.config(text="Moving Forward")
    reset_labels()
    forward_label.config(bg="grey", fg="white")
    speed_label.config(text="100%")
    speed_bar.config(value=100)
    # steering_label.config(text="Steering: 0%")
    update_steering_indicator(0)

def move_backward():
    bluetooth.send_command(bluetooth.backward)
    label.config(text="Moving Backward")
    reset_labels()
    backward_label.config(bg="grey", fg="white")
    speed_label.config(text="60%")
    speed_bar.config(value=60)
    # steering_label.config(text="Steering: 0%")
    update_steering_indicator(0)

def move_left():
    bluetooth.send_command(bluetooth.left)
    label.config(text="Moving Left")
    reset_labels()
    left_label.config(bg="grey", fg="white")
    speed_label.config(text="50%")
    speed_bar.config(value=50)
    # steering_label.config(text="Steering: -50%")
    update_steering_indicator(-50)

def move_right():
    bluetooth.send_command(bluetooth.right)
    label.config(text="Moving Right")
    reset_labels()
    right_label.config(bg="grey", fg="white")
    speed_label.config(text="50%")
    speed_bar.config(value=50)
    # steering_label.config(text="Steering: 50%")
    update_steering_indicator(50)

def stop():
    bluetooth.send_command(bluetooth.stop)
    label.config(text="Stopped")
    reset_labels()
    stop_label.config(bg="grey", fg="white")
    speed_label.config(text="0%")
    speed_bar.config(value=0)
    # steering_label.config(text="Steering: 0%")
    update_steering_indicator(0)

def mic():
    label.config(text="Using Mic")
    reset_labels()
    mic_label.config(bg="grey", fg="white")
    speed_label.config(text="100%")
    speed_bar.config(value=100)
    # steering_label.config(text="Steering: 0%")
    update_steering_indicator(0)
    word = speechToWord.get_word_from_speech()
    bluetooth.send_command(bluetooth.word_to_command(word))

def reset_labels():
    forward_label.config(bg="white", fg="black")
    backward_label.config(bg="white", fg="black")
    left_label.config(bg="white", fg="black")
    right_label.config(bg="white", fg="black")
    stop_label.config(bg="white", fg="black")


# Create a Canvas widget
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Constants for steering indicator
steering_radius = 100  # Radius of the circular steering indicator
steering_center_x = 150  # X-coordinate of the center of the steering indicator
steering_center_y = 150  # Y-coordinate of the center of the steering indicator

# Draw the circular steering indicator
canvas.create_oval(
    steering_center_x - steering_radius,
    steering_center_y - steering_radius,
    steering_center_x + steering_radius,
    steering_center_y + steering_radius,
    outline="black",
    width=2
)

# Draw the initial steering pointer
steering_pointer = canvas.create_line(
    steering_center_x,
    steering_center_y,
    steering_center_x,
    steering_center_y - steering_radius,
    fill="red",
    width=2
)


def update_steering_indicator(steering_percentage):
    steering_angle = (steering_percentage / 100) * (2 * pi)
    x = int(steering_radius * cos(steering_angle))
    y = int(steering_radius * sin(steering_angle))
    canvas.coords(steering_pointer, steering_center_x, steering_center_y, steering_center_x + x, steering_center_y + y)
    steering_label.config(text="Steering: {}%".format(steering_percentage))

root = tk.Tk()
root.title("Robot Controller")

# Styling options
root.configure(bg="white")  # Set background color of the window


label = tk.Label(root, text="Robot Controller", font=("Arial", 24), fg="black", bg="white")
label.pack(pady=20)

# Label frame
label_frame = tk.Frame(root)
label_frame.pack(pady=10)

# Labels
forward_label = tk.Label(label_frame, text="FORWARD", font=("Arial", 24), fg="black", bg="white")
forward_label.grid(row=0, column=1, padx=5, pady=5)

backward_label = tk.Label(label_frame, text="BACKWARD", font=("Arial", 24), fg="black", bg="white")
backward_label.grid(row=2, column=1, padx=5, pady=5)

left_label = tk.Label(label_frame, text="LEFT", font=("Arial", 24), fg="black", bg="white")
left_label.grid(row=1, column=0, padx=5, pady=5)

right_label = tk.Label(label_frame, text="RIGHT", font=("Arial", 24), fg="black", bg="white")
right_label.grid(row=1, column=2, padx=5, pady=5)

stop_label = tk.Label(label_frame, text="STOP", font=("Arial", 24), fg="black", bg="white")
stop_label.grid(row=1, column=1, padx=5, pady=5)

mic_label = tk.Label(label_frame, text="Mic", font=("Arial", 24), fg="black", bg="white")
mic_label.grid(row=2, column=2, padx=5, pady=5)


steering_label = tk.Label(root, text="Steering: 0%", font=("Arial", 18), fg="black", bg="white")
steering_label.pack(pady=10)


speed_frame = tk.Frame(root)
speed_frame.pack(pady=10)

speed_label = tk.Label(speed_frame, text="0%", font=("Arial", 24), fg="black", bg="white")
speed_label.pack(pady=10)

speed_bar = ttk.Progressbar(speed_frame, orient="horizontal", length=300, mode="determinate")
speed_bar.pack()


# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
forward_button = tk.Button(button_frame, text="FORWARD", command=move_forward, width=10)
forward_button.grid(row=0, column=1, padx=5, pady=5)

backward_button = tk.Button(button_frame, text="BACKWARD", command=move_backward, width=10)
backward_button.grid(row=2, column=1, padx=5, pady=5)

left_button = tk.Button(button_frame, text="LEFT", command=move_left, width=10)
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(button_frame, text="RIGHT", command=move_right, width=10)
right_button.grid(row=1, column=2, padx=5, pady=5)

stop_button = tk.Button(button_frame, text="STOP", command=stop, width=10)
stop_button.grid(row=1, column=1, padx=5, pady=5)

mic_button = tk.Button(button_frame, text="MIC", command=mic, width=10)
mic_button.grid(row=2, column=2, padx=5, pady=5)



root.mainloop()