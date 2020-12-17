import RPi.GPIO as GPIO
import time, math
import pygame
# import PySimpleGUI as gui
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# gui.theme('Topanga')

pygame.init()


def sensors():
    students = 0

    pulse_start = 0
    pulse_end = 0
    pulse_duration = 0
    distance = 0

    pulse_start2 = 0
    pulse_end2 = 0
    pulse_duration2 = 0
    distance2 = 0

    TRIG = 23
    ECHO = 24

    TRIG2 = 27
    ECHO2 = 22

    running = True

    (width, height) = (900, 600)
    white = (255, 255, 255)

    # Pygame Stuff that wasnt working
    '''
    myFont = pygame.font.SysFont("Times New Roman", 30)
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Number of Students")
    displayStudentsLabel= myFont.render("Number of Students in your classroom: ", 1, white)
    displayStudents = myFont.render(str(students), 1, white)
    '''

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO2, GPIO.IN)

    # ------------------------------#
    # layout = [[gui.Text("Here are the results!")], [gui.Text(students)],  [gui.Button("Reset")]]
    # window = gui.Window("Number of Students", layout)
    # ------------------------------#

    try:
        while running:

            GPIO.output(TRIG, False)
            time.sleep(0.2)

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = round(pulse_duration * 17150, 0)
            '''
            print("Sensor 1 : ", distance)
            '''

            '''
            if distance <= 10:
                students = students + 1
                print(students)
            else:
                print(students)
            '''

            GPIO.output(TRIG2, False)
            time.sleep(0.1)

            GPIO.output(TRIG2, True)
            time.sleep(0.00001)
            GPIO.output(TRIG2, False)

            while GPIO.input(ECHO2) == 0:
                pulse_start2 = time.time()

            while GPIO.input(ECHO2) == 1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2

            distance2 = round(pulse_duration2 * 17150, 0)

            '''
            print("Sensor 2 : ", distance2)
            '''

            '''
            if distance2 <= 10:
                students = students - 1
                print(students)
            else:
                print(students)
            '''

            if distance <= 70 and distance2 >= 79:
                students += 1
                print(students)
                time.sleep(1)

            elif distance2 <= 78 and distance >= 71:
                students -= 1
                print(students)
                time.sleep(1)

            else:
                print(students)

                # event, values = window.read()
                # if event == gui.WIN_CLOSED:
                # break

                # window.close()
                # More Pygame stuff
                '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pygame.display.update()
                screen.blit(displayStudentsLabel, (200, 20))
                screen.blit(displayStudents, (200, 60))

        pygame.quit()
        '''



    except KeyboardInterrupt:
        print("Cleaning Up!")
        GPIO.cleanup()


sensors()
