import cocos

class Objects(cocos.layer.Layer):
    def __init__(self,name,image,xy):
        super().__init__()
        self.xy = xy
        self.name = name
        self.a = cocos.sprite.Sprite(image)
        self.do(cocos.actions.interval_actions.MoveTo((xy[0]*32+16,xy[1]*32+16), 0))
        self.add(self.a)

    def moveTo(self,x,y,time):
        self.xy = [x,y]
        self.do(cocos.actions.interval_actions.MoveTo((self.xy[0]*32+16,self.xy[1]*32+16), time))
    
    def nowXY(self):
        return self.xy