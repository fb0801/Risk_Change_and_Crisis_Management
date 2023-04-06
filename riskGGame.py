import pygame
import os

import tkinter as tk
import math
import random
from tkinter import messagebox
from playsound import  playsound
from pygame import mixer

pygame.font.init()#use font lib
pygame.mixer.init()#allow us to use sounds

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('Risk Game')#title of the game

