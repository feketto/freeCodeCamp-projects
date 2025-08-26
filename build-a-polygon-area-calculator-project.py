class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self,n_width):
        self.width = n_width
    
    def set_height(self,n_height):
        self.height = n_height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            picture = ''
            for i in range(self.height):
                picture += f"{'*' * self.width}\n"
            return picture
        else:
            return 'Too big for picture.' 
    
    def get_amount_inside(self, second):
        times_width = self.width / second.width
        times_height = self.height / second.height
        return int(times_width * times_height)
        
        
    
        
        
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, n_side):
        self.width = n_side
        self.height = n_side

    def set_width(self,n_side):
        self.width = n_side
        self.height = n_side
    
    def set_height(self,n_side):
        self.height = n_side
        self.width = n_side
