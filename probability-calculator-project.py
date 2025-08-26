import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, value in kwargs.items():
            for _ in range(value):
                self.contents.append(color)
        self.original_contents = self.contents[:]


    def __str__(self):
        return str(self.contents).strip('[]')


    def draw(self, to_draw):
        if to_draw >= len(self.contents):
            self.contents.clear()
            return self.original_contents
        else:
            drawn_content = random.sample(self.contents, to_draw)
            for i in drawn_content:
                self.contents.remove(i)
            return drawn_content
        



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):

        temp_hat = copy.deepcopy(hat)

        drawn_balls = temp_hat.draw(num_balls_drawn)
        
        is_successful = True
        for color, expected_count in expected_balls.items():
            if drawn_balls.count(color) < expected_count:
                is_successful = False
                break  
        if is_successful:
            success += 1
    return success / num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
print(experiment(hat1, {'red':2,'green':1}, 50, 200))
