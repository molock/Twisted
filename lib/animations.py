#list of animations to import

import pygame
from pygame import *
from pygame.image import *
from pygame.locals import *
import data

ANIMATION_PLAYER_WALK = None
ANIMATION_PLAYER_STILL = None
ANIMATION_PLAYER_RUN = None
ANIMATIONS_PLAYER = None


def load_animations():
	global ANIMATION_PLAYER_STILL
	global ANIMATIONS_PLAYER
	ANIMATION_PLAYER_WALK = [data.load_image("bizniezwalkin.png")]
	ANIMATION_PLAYER_STILL = [data.load_image("bizstill.png")]
	ANIMATION_PLAYER_RUN = [data.load_image("bizniezrun.gif")]

	ANIMATIONS_PLAYER = [ANIMATION_PLAYER_STILL, ANIMATION_PLAYER_WALK, ANIMATION_PLAYER_RUN]
	
def load_player():
	#load player animations and return the list
	#ANIMATION_PLAYER_WALK = [data.load_image("bizniezwalkin.png")]
	ANIMATION_PLAYER_WALK = [[10],[data.load_image("pngconverts/bizneztimewalk1.png"),data.load_image("pngconverts/bizneztimewalk2.png"),data.load_image("pngconverts/bizneztimewalk3.png"),data.load_image("pngconverts/bizneztimewalk4.png")]]
	ANIMATION_PLAYER_STILL = [[15],[data.load_image("pngconverts/bizneztimestand1.png"),data.load_image("pngconverts/bizneztimestand2.png"),data.load_image("pngconverts/bizneztimestand3.png")]]
	ANIMATION_PLAYER_JUMP = [[20],[data.load_image("pngconverts/bizneztimejump1.png"),data.load_image("pngconverts/bizneztimejump2.png"),data.load_image("pngconverts/bizneztimejump3.png")]]
	ANIMATION_PLAYER_BLOCK = [[15],[data.load_image("pngconverts/bizneztimeblock.png")]]
	ANIMATION_PLAYER_THROW = [[15],[data.load_image("pngconverts/bizneztimethrow1.png"),data.load_image("pngconverts/bizneztimethrow2.png"),data.load_image("pngconverts/bizneztimethrow3.png"),data.load_image("pngconverts/bizneztimethrow4.png")]]
	print "loaded fine"
	#ANIMATION_PLAYER_RUN = [data.load_image("biznestimerun1.png"),data.load_image("/pngconverts/biznestimerun2.png"),data.load_image("pngconverts/biznestimerun3.png"),data.load_image("pngconverts/biznestimerun4.png")]
	ANIMATION_PLAYER_RUN = [[10],[data.load_image("pngconverts/bizneztimerun1.png"),data.load_image("pngconverts/bizneztimerun2.png"),data.load_image("pngconverts/bizneztimerun3.png"),data.load_image("pngconverts/bizneztimerun4.png")]]
	
	ANIMATIONS_PLAYER = [ANIMATION_PLAYER_STILL, ANIMATION_PLAYER_WALK, ANIMATION_PLAYER_RUN,ANIMATION_PLAYER_JUMP,ANIMATION_PLAYER_BLOCK,ANIMATION_PLAYER_THROW]
	return ANIMATIONS_PLAYER
	
def load_robot_flying():
	ANIMATION_ROBOT_WALK = [[20],[data.load_image("pngconverts/robotchase1.png"),data.load_image("pngconverts/robotchase2.png"),data.load_image("pngconverts/robotchase3.png")]]
	ANIMATION_ROBOT_DIVE = [[40],[data.load_image("pngconverts/robotchase1.png")]]
	
	ANIMATIONS_ROBOT = [ANIMATION_ROBOT_WALK,ANIMATION_ROBOT_DIVE]
	return ANIMATIONS_ROBOT
	
def load_robot_chase1():
	ANIMATION_ROBOT_WALK = [[15],[data.load_image("pngconverts/smallrobotchase1.png"),data.load_image("pngconverts/smallrobotchase2.png"),data.load_image("pngconverts/smallrobotchase3.png"),data.load_image("pngconverts/smallrobotchase2.png")]]
	ANIMATION_ROBOT_STILL = [[50],[data.load_image("pngconverts/smallrobotchase1.png")]]
	
	ANIMATIONS_ROBOT = [ANIMATION_ROBOT_STILL,ANIMATION_ROBOT_WALK,ANIMATION_ROBOT_WALK,ANIMATION_ROBOT_WALK]
	return ANIMATIONS_ROBOT
	
def info_robot_chase1():
	INFO_NAME = "chaser"
	INFO_MOVEMENT = "ground"
	return [INFO_NAME,INFO_MOVEMENT]
	
def info_robot_flying():
	INFO_NAME = "Robothulu"
	INFO_MOVEMENT = "flying"
	return [INFO_NAME,INFO_MOVEMENT]
	
def info_objects():
	#return lists of data for each object type in the game
	#['name','image'.. maybe turn image into animations later..]
	OBJ_BOOTH = ["booth",data.load_image("objects/phonebooth.png")]
	OBJ_STAPLER = ["stapler",data.load_image("objects/stapler.png")]
	OBJ_TPSBOX = ["tpsbox",data.load_image("objects/tpsbox.png")]
	
	#0-booth 1-stapler 2-tpsbox
	OBJECTS = [OBJ_BOOTH,OBJ_STAPLER,OBJ_TPSBOX]
	return OBJECTS
	
