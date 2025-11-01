import random

class Color:
	def __init__(self,r:int,g:int,b:int):
		self.r = r
		self.g = g
		self.b = b


class Check:
	def red_checker(bg:Color,fg:Color):
		if bg.r - fg.r >  20:
			return 1
		else: 
			return 0
	
	def blue_checker(bg:Color,fg:Color):
		if bg.b - fg.b > 20:
			return 1
		else:
			return 0
	
	def green_checker(bg:Color,fg:Color):
		if bg.g - fg.g > 20:
			return 1
		else:
			return 0


class Pallate:
	def __init__(self,bg:Color,fg:Color):
		self.bg = bg
		self.fg = fg

	def check(self):
		if Check.red_checker(self.bg,self.fg ) == 1 and Check.blue_checker(self.bg,self.fg) == 1 and Check.green_checker(self.bg,self.fg) == 1:
			return True
		# elif Check.blue_checker(self.bg,self.fg) == 0:
		# 	return False
		# elif Check.green_checker(self.bg,self.fg) == 0:
		# 	return False
		
		else:
			return False
		
			
color_01 = Color(r=random.randint(1,50),g=random.randint(1,50),b=random.randint(1,50))
color_02 = Color(r=random.randint(1,50),g=random.randint(1,50),b=random.randint(1,50))

p = Pallate(bg=color_01,fg=color_02)

print(p.check())


