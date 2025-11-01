class Color:
	def __init__(self,r:int,g:int,b:int):
		self.r = r
		self.g = g
		self.b = b


class Check:
	
	def red_checker(bg:Color,fg:Color):
		if bg.r - fg.r <   10:
			return 0 
		return 1
	
	def blue_checker(bg:Color,fg:Color):
		if bg.b - fg.b < 10:
			return 0
		return 1
	
	def green_checker(bg:Color,fg:Color):
		if bg.g - fg.g < 10:
			return 0
		return 1


class Pallate:
	def __init__(self,bg:Color,fg:Color):
		self.bg = bg
		self.fg = fg

	def check(self):
		if Check.red_checker(self.bg,self.fg ) == 0 and Check.blue_checker(self.bg,self.fg) == 0 and Check.green_checker(self.bg,self.fg) == 0:
			return False
		# elif Check.blue_checker(self.bg,self.fg) == 0:
		# 	return False
		# elif Check.green_checker(self.bg,self.fg) == 0:
		# 	return False
		
		else:
			return True
		
			
color_01 = Color(r=100,g=100,b=100)
color_02 = Color(r=6,g=3,b=40)

p = Pallate(bg=color_01,fg=color_02)

print(p.check())


