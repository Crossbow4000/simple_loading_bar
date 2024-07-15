class LoadingBar:
    def __init__(self, max_value, length=50, show_percentage=True, show_progress=True, filled='#', empty='-', starting_operation = ''):
        self.value = 0
        self.max_value = max_value
        self.length = length
        self.show_percentage = show_percentage
        self.show_progress = show_progress
        self.filled = filled
        self.empty = empty
        self.current_operation = starting_operation
        self.previous_length = 0
    def _display(self):
        percent_filled = round(self.value / self.max_value, 2)
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]  '
        bar_string += self.current_operation
        if self.previous_length > len(bar_string):
            print(f'\r{" "*self.previous_length}', end='')
        print(bar_string, end='')
        self.previous_length = len(bar_string)
    def _end(self):
        percent_filled = self.value / self.max_value
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]'
        print(f'\r{" "*self.previous_length}', end='')
        print(bar_string)
    def set_value(self, new_value, current_operation=''):
        self.value = new_value
        self.current_operation = current_operation if current_operation != '' else self.current_operation
        if self.value < self.max_value:
            self._display()
        else:
            self._end()
    def increment(self, current_operation=''):
        self.value += 1
        self.current_operation = current_operation if current_operation != '' else self.current_operation
        if self.value < self.max_value:
            self._display()
        else:
            self._end()
