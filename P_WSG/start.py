import cocos
from cocos.director import director
import lib.experimentalScene as experimentalScene

if __name__ == "__main__" :

    director.init(1280, 720, 'warShipGirl')
    director.run(experimentalScene.get_scene())