import sys, time
# Here, we import two built-in libraries - functions, variables, etc. that have already been defined and that we can call on.

import RPi.GPIO as GPIO

# This is a Raspbian library that allows us to use Python to control GPIO pins.

redPin = 11
greenPin = 15
bluePin = 13


# Now, we define some variables - which pins we'll be connecting to which RGB lead. This step isn't necessary, but it makes it easier to change pins if you need to.

def blink(pin):
    # Here, we define a function. A function is a set of steps that the computer will execute in the order that we give to it. This particular function will require one variable in order to run: the number of the pin that we want to light up.

    GPIO.setmode(GPIO.BOARD)
    # We start our function off by referencing one of our libraries, GPIO. Then, we tell it that we want to choose a naming convention for the GPIO pins (of which there are two), so that the program knows which ones we're referring to. Then, we tell it to use the "board" convention (rather than the BMC convention), again using the GPIO library.

    GPIO.setup(pin, GPIO.OUT)
    # Now, once again using the GPIO library, we tell the Pi that we want to use a pin. But first, we need to specify which pin and how we want to use it - input or output. Here, "pin" is the variable that will be plugged into blink(pin).

    GPIO.output(pin, GPIO.HIGH)


# Now that the pin has been set up, this line turns it on. You should recognize the syntax by now; here we're using the same variable "pin" and using the GPIO library to set the pin to a value of "high". In the case of GPIO pins, a "high" value results in 3.3v being passed, or "on", whereas a "low" value results in 0v being passed, or "off".

# Now we're going to define a function to turn lights off. It's going to look almost identical to the previous function, only we'll be setting the pins back to low.

def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


# We need to define some functions specific to color using the functions we just made. Recall that we're using pins 11, 13, and 15 for red, green, and blue. We'll start with functions that turn lights on. With this type of function, we won't require any parameters, so the brackets stay empty; calling this function later in the program will simply execute it.

def redOn():
    blink(redPin)


# Here, we give the "blink" function a pin number to use, 11. When we call redOn(), our blink function will begin executing with "pin" replaced by "redPin". Recall that, earlier, we set redPin equal to 11.

# Now we do the same thing for the rest of the colors.

def greenOn():
    blink(greenPin)


def blueOn():
    blink(bluePin)


# Remember that when dealing with light, yellow is made by mixing red with green, cyan using green and blue, magenta with red and blue, and white by combining all three.

def yellowOn():
    blink(redPin)
    blink(greenPin)


def cyanOn():
    blink(greenPin)
    blink(bluePin)


def magentaOn():
    blink(redPin)
    blink(bluePin)


def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)


# Finally, we write the functions to turn lights off. Again, the syntax will be similar to the functions above.

def redOff():
    turnOff(redPin)


def greenOff():
    turnOff(greenPin)


def blueOff():
    turnOff(bluePin)


def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)


def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)


def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)


def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


# Now we're ready to define our main function; a loop that will constantly ask for user input and react by calling various functions. In this case, the user will be able to turn colors on and off. This program is written so that it will only accept a few pre-specified inputs. Otherwise, it will do nothing and display a message to that effect.

# Again, we're not asking for any variables with this function, so the brackets stay empty. "while True" essentially says "while the program is running, do this", so it will run constantly until we quit.

def main():
    while True:
        cmd = raw_input("Choose an option:")
        # We define a new variable "cmd" to use later and set it equal to the user's input. It will also constantly prompt the user to choose an option.

        # Now an "if" statement that will run only if the user input exactly matches the text within the quotation marks. Note that here we use two "equal to" symbols. In Python, and indeed most languages, a single "equal to" is used to change the value of a variable while doubles are used to compare whether or not variable values match each other.

        if cmd == "red on":
            redOn()
        # "elif" stands for "else, if". This tacks onto the earlier "if" statement and adds new parameters, allowing us to create a chain of "else, if" statements easily.

        elif cmd == "red off":
            redOff()

        elif cmd == "green on":
            greenOn()

        elif cmd == "green off"
            greenOff()

        elif cmd == "blue on":
            blueOn()

        elif cmd == "blue off":
            blueOff()

        elif cmd == "yellow on":
            yellowOn()

        elif cmd == "yellow off":
            yellowOff()

        elif cmd == "cyan on":
            cyanOn()

        elif cmd == "cyan off":
            cyanOff()

        elif cmd == "magenta on":
            magentaOn()

        elif cmd == "magenta off":
            magentaOff()

        elif cmd == "white on":
            whiteOn()

        elif cmd == "white off":
            whiteOff()

        else:
            print("Not a valid command.")

    return


# With our last "else" statement, if the user attempts to input anything other than one of the commands specified above, it will tell the user that it is an invalid command. The last thing the function needs is that "return" so the program knows when to loop.

main()
# This is the last line of our code. When the program is run, this line will call the main function that we just defined and the loop will be set.