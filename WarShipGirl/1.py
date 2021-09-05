import codecs
import cocos
from cocos.layer import Layer
from cocos.actions import *
from cocos.text import Label
from cocos.director import director

line_num=1
def readfile(num):
    count=0
    file=codecs.open("test.txt",'r','UTF-8')
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            count+=1
            if count==num:
                return line
    file.close()

class HelloWorld(Layer):
   def __init__(self):
      super(HelloWorld,self).__init__()
      self.count=0 
      self.lable=cocos.text.Label('', font_name='Times New Roman', font_size=32)
      self.lable.position = 50,30
      self.add(self.lable)
      self.lable.do(Repeat(Delay(0.1)+CallFunc(self.autoword)))
   def autoword(self): 
      word="Hello, World!" 
      while self.count < len(word):
          self.lable.element.text=self.lable.element.text+word[self.count] 
          self.count+=1
          break
   def on_key_press(self,k,m):
      global line_num
      if key.ENTER in self.keys_pressed:
            self.lable.element.text=""
            line_num+=1
            self.count=0

if __name__ == '__main__':

    director.init(1280,720,'new')
    hello_layer = HelloWorld()
    test_scene = cocos.scene.Scene(hello_layer)

    director.run(test_scene)
