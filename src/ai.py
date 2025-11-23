import random

class Color:
	def __init__(self,r:int,g:int,b:int):
		self.r = r
		self.g = g
		self.b = b


class Check:
    # 
	def red_checker(bg:Color,fg:Color):
		return 1 if bg.r - fg.r > 50 else 0

	
	def blue_checker(bg:Color,fg:Color):
		return 1 if bg.g - fg.g > 50 else 0
	
	def green_checker(bg:Color,fg:Color):
		return 1 if bg.b - fg.b > 50 else 0


class Pallate:
	def __init__(self,bg:Color,fg:Color):
		self.bg = bg
		self.fg = fg

	def check(self):
		return True if Check.red_checker(self.bg,self.fg) == 1 and Check.blue_checker(self.bg,self.fg) == 1 and Check.green_checker(self.bg,self.fg) == 1 else False
	
        
		


if __name__ == '__main__':
    count = int(input('How many pallate?'))
    for i in range(count):

        color_01 = Color(r=random.randint(1,255),g=random.randint(1,255),b=random.randint(1,255))
        color_02 = Color(r=random.randint(1,255),g=random.randint(1,255),b=random.randint(1,255))

        p = Pallate(bg=color_01,fg=color_02)

        print(p.check())


