import sys

class LoadingBar:
    def __init__(self, max_value, length=50, show_percentage=True, show_progress=True, filled='#', empty='-'):
        self.value = 0
        self.max_value = max_value
        self.length = length
        self.show_percentage = show_percentage
        self.show_progress = show_progress
        self.filled = filled
        self.empty = empty

    def display(self):
        percent_filled = round(self.value / self.max_value, 2)
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]'
        print(bar_string, end='')
    def end(self):
        percent_filled = self.value / self.max_value
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]'
        print(bar_string)
    def update(self, new_value=0, increment=False):
        self.value = new_value if not increment else self.value + 1
        if self.value < self.max_value:
            self.display()
        else:
            self.end()
