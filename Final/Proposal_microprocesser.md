# Final Project Proposal

## Title

Haptic Compass Belt

## Summary

My project is about crafting a belt that vibrates where north is. This is based on the concept that wearing a belt like this consistently will cause the brain to interpret the vibrations as a sense separate from touch, providing an innate sense of direction.

## Details

The setup will consist of a [microprocessor](https://www.adafruit.com/product/5786), a [magnetic field sensor](https://www.adafruit.com/product/4413), and 8 [coin vibrator motors](https://www.adafruit.com/product/1201) (N, NE, E, etc). The software will connect the field sensor and the motors to the microprocessor. It will softly calibrate the magnetic field sensor (an in depth calibration cannot run on a microprocessor) by recording the minimum and maximum values for each axis for 10 seconds on start (if the new recorded min value is less than the previously stored value, it will replace the min value with the new recorded value. If none of the values have updated like this for more than 1 second, it will end the code and pass the min and max values for each axis onward. I still don't understand what happens next but I'll research it.

Then the program will take the magnetic field values and use them to calculate the heading. Based on that it will vibrate whichever motor is closest to north. The motors, sensor, and microprocessor will be attached to a belt. A USB battery pack will go in a pocket.

The magnetic field sensor also acts as a button and can respond to taps. It will be used as a button to change the mode from continuous pulse to two pulses that occur when the orientation is changed.

## GOOD Outcome

The microprocessor is connected to the sensor and motors and is able to communicate with them.

## BETTER Outcome

The program is able to calculate the heading and vibrate the correct motor. There might be calibration issues. Starting the belt might be difficult and require the computer to set it up.

## BEST Outcome

The belt can turn on and function by itself. Tapping is able to calibrate it when needed, and switch modes between continuous vibrations and pulses when orientation is changed.



## Next Steps

1. Purchase components
2. Install CircuitPython by following the circuitPython documentation start guide (below).
3. Read documentation for the compass and follow the instruction for how to attach the compass to the microprocessor, how to install libraries, and how to set up the calibration code. Test the code using the print example in the documentation (prints the microTeslas of each axis).
4. Analyze the two reference code examples. Observe where the motors are attached in the diagram for the belt compass example. Attach the motors to similar out pins.
5. Analyze how each reference is calculating the heading. Copy or convert that code.
6. Analyze how the belt compass reference sends messages to each motor to vibrate based on the heading. Copy or convert that code.

Other/general:
- review on soldering (I haven't soldered since high school)
- the specific functions used to interact with in/outs on the microprocessor

## Resources

- [Circuit Python that works with my chosen microprocessor](https://circuitpython.org/board/adafruit_metro_rp2040/)
- [CircuitPython documentation](https://learn.adafruit.com/welcome-to-circuitpython/overview)
- [Accelerometer + Compass Breakout Documentation](https://cdn-learn.adafruit.com/downloads/pdf/lsm303-accelerometer-slash-compass-breakout.pdf)
- [Github page of someone who already made this project, coded in Arduino](https://github.com/kylecorry31/compass-belt/blob/master/compass_belt/Compass.cpp)
- [Article with reference code for a digital compass display](https://www.engineersgarage.com/arduino-digital-compass-hmc5883l-ssd1306-oled/)
- [Declination calculator](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml)

Other physical materials not listed above:
- [Soldering iron](https://www.amazon.com/Liouhoum-Auto-Sleep-Adjustable-Temperature-Thermostatic/dp/B08PZBPXLZ/ref=asc_df_B08PZBPXLZ/?tag=hyprod-20&linkCode=df0&hvadid=475794938858&hvpos=&hvnetw=g&hvrand=14249129053555422662&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9002059&hvtargid=pla-1174022853327&mcid=bf248453f91f34dea3e243efb765ed47&gclid=CjwKCAjw8diwBhAbEiwA7i_sJQ_hteIQhsJC0OPJvqrG-54-5vJxgPH2qbwjRzRZPYsMPTOFTEAITBoC-hMQAvD_BwE&th=1)

