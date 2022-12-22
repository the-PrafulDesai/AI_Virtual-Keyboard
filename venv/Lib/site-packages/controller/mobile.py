class Mobile:
    
    def __init__(self,id,help=False):
        self.id = id
        self.help = help
        self.gx, self.gy, self.gz = 0, 0, 0
        self.ax, self.ay, self.az = 0, 0 ,0
        self.angle = 0
        self.size = 100
        self.text  = ''

    def handle(self,data):
        try:
            evnType = data['evnType']

            if evnType == 'Tap':
                x = data['x']
                y = data['y']
                self.onTap(x,y)

            elif evnType == 'Long Press':
                x = data['x']
                y = data['y']
                self.onLongPress(x,y)

            elif evnType == 'Pinch':
                x = data['x']
                y = data['y']
                d = data['d']
                self.onPinch(x,y,d)
            
            elif evnType == 'Text':
                text = data['text']
                self.text = text
                self.onText(text)

            elif evnType == 'RTD':
                ax = data['ax']
                ay = data['ay']
                az = data['az']
                gx = data['gx']
                gy = data['gy']
                gz = data['gz']
                angle = data['angle']
                size = data['size']
                self.setAccelerometer(ax,ay,az)
                self.setGyroscope(gx,gy,gz)
                self.angle = angle
                self.size = size

            elif evnType == 'Double Tap':
                x = data['x']
                y = data['y']
                self.onDoubleTap(x,y)

            elif evnType == 'Flick':
                x = data['x']
                y = data['y']
                px = data['px']
                py = data['py']
                v = data['v']
                self.onFlick(x,y,px,py,v)

        except BaseException as e:
            print(data,e)

    def getGyroscope(self):
        return self.gx, self.gy, self.gz

    def setGyroscope(self,gx,gy,gz):
        self.gx, self.gy, self.gz = gx, gy, gz
    
    def getAccelerometer(self):
        return self.ax, self.ay, self.az
        
    def setAccelerometer(self,ax,ay,az):
        self.ax, self.ay, self.az = ax, ay, az
    
    def getAngle(self):
        return self.angle

    def getSize(self):
        return self.size

    def onTap(self,x,y):
        if self.help:
            print('[TAP DETECTED] You can overwrite onTap(x,y) to handle it.')
    
    def onDoubleTap(self,x,y):
        if self.help:
            print('[DOUBLE TAP DETECTED] You can overwrite onDoubleTap(x,y) to handle it.')
    
    def onFlick(self,x,y,px,py,v):
        if self.help:
            print('[FLICK DETECTED] You can overwrite onFlick(x,y,px,py,v) to handle it.')
    
    def onLongPress(self,x,y):
        if self.help:
            print('[LONGPRESS DETECTED] You can overwrite onLongPress(x,y) to handle it.')
    
    def onPinch(self,x,y,d):
        if self.help:
            print('[PINCH DETECTED] You can overwrite onPinch(x,y,d) to handle it.')

    def on_left_swipe(self):
        if self.help:
            print('[LEFT SWIPE DETECTED] You can overwrite on_left_swipe to handle it.')

    def on_right_swipe(self):
        if self.help:
            print('[RIGHT SWIPE DETECTED] You can overwrite on_right_swipe to handle it.')

    def on_up_swipe(self):
        if self.help:
            print('[UP SWIPE DETECTED] You can overwrite on_up_swipe to handle it.')

    def on_down_swipe(self):
        if self.help:
            print('[DOWN SWIPE DETECTED] You can overwrite on_down_swipe to handle it.')
    
    def onText(self,text):
        if self.help:
            print('[TEXT DETECTED] You can overwrite onText(text) to handle it.')
    