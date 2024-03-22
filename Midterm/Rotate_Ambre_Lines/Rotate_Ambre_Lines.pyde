sine_wave = []

def setup():
    size(400,400)
    noFill()
    for i in range(width/3):
        radian = map(i, 0, width/3, 0, PI)
        sine_wave.append(abs(sin(radian)))
        
def draw():
    translate(width/2, height/2)
    for i in range(width/3):
        stroke(sine_wave[i] * 255)
        rotate(PI/12)
        #triangle(i, 0, i, height/3, 0,0)
        line(i, 0, i, height/3)
        
