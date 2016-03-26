#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
[Function]

[Date]
2016-03-26 

[Author]
linx

[Contact]
-------------------------------------------------------------------------------
"""
 
#---------------------------------import---------------------------------------
import cocos
#------------------------------------------------------------------------------

###############################################################################

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super( HelloWorld, self ).__init__()
        label = cocos.text.Label('Hello, world', font_name = 'Times New Roman', font_size = 32, anchor_x = 'center', anchor_y = 'center')
        label.position = 320, 240
        self.add(label)
        
    
if __name__=="__main__":
    cocos.director.director.init()
    hello_layer = HelloWorld()
    main_scene = cocos.scene.Scene(hello_layer)
    cocos.director.director.run(main_scene)
    #cocos.director.director.run( cocos.scene.Scene( HelloWorld() ) )
