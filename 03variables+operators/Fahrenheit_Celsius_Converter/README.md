# Fahrenheit and Celsius Converter

I wanted to continue asking for which temperature unit to convert to until the user types either F or C.
The main issue was that typing anything satisfied the if for converting from C to F. 
* `if F_or_C == 'f' or 'F':` did not work, any input for F_or_C satisfies it.
* `if '{F_or_C}' == 'f' or 'F':` did not work, any input for F_or_C satisfies it.
* Putting the check under another if that checks if it is greater length than 0 works.

</br> I then realized that I can put everything in a loop function. I used while True.
* It continues looping. Each loop it checks the user input. If it was longer than 0 characters, it continues. If it was F, it converts to F. If it was C, it converts to C. If it was 0 characters or wasn't F or C (case-sensitive), it repeats the question (type either F or C). This way it also loops again after one conversion so the user can do multiple conversions without restarting the program.

