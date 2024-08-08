class LoadingBar:
    """
    A class to represent a progress bar in the console.

    Attributes:
        max_value (int): The maximum value of the progress bar.
        length (int): The length of the progress bar in characters.
        show_percentage (bool): Whether to display the percentage completion.
        show_progress (bool): Whether to display the current progress value.
        filled (str): Character used for the filled portion of the bar.
        empty (str): Character used for the empty portion of the bar.
        starting_operation (str): Initial operation message to display.

    Methods:
        set_value(new_value, current_operation=''): Sets the progress bar to a new value and updates the display.
        increment(current_operation=''): Increments the progress bar by one and updates the display.
    """
    def __init__(self, max_value, length=50, show_percentage=True, show_progress=True, filled='#', empty='-', starting_operation=''):
        '''
        Initializes a LoadingBar instance.

        Parameters:
            max_value (int): The maximum value of the progress bar.
            length (int, optional): The length of the progress bar. Defaults to 50.
            show_percentage (bool, optional): Whether to display the percentage of completion. Defaults to True.
            show_progress (bool, optional): Whether to display the current progress value. Defaults to True.
            filled (str, optional): The character used to represent the filled portion of the bar. Defaults to '#'.
            empty (str, optional): The character used to represent the empty portion of the bar. Defaults to '-'.
            starting_operation (str, optional): The initial operation message to display. Defaults to ''.
        '''
        self.value = 0
        self.max_value = max_value
        self.length = length
        self.show_percentage = show_percentage
        self.show_progress = show_progress
        self.filled = filled
        self.empty = empty
        self.current_operation = starting_operation
        self._previous_length = 0

    
    def set_value(self, new_value, current_operation=''):
        '''
        Sets the current value of the loading bar and updates the display.

        Parameters:
            new_value (int): The new value to set for the progress bar.
            current_operation (str, optional): The operation message to display. Defaults to ''.
        '''
        self.value = new_value
        self.current_operation = current_operation if current_operation != '' else self.current_operation
        if self.value < self.max_value:
            self._display()
        else:
            self._end()

    def increment(self, current_operation=''):
        '''
        Increments the current value of the loading bar by 1 and updates the display.

        Parameters:
            current_operation (str, optional): The operation message to display. Defaults to ''.
        '''
        self.value += 1
        self.current_operation = current_operation if current_operation != '' else self.current_operation
        if self.value < self.max_value:
            self._display()
        else:
            self._end()

    def _display(self):
        '''
        Updates the display of the loading bar in the console.
        '''
        percent_filled = round(self.value / self.max_value, 2)
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]  '
        bar_string += self.current_operation
        if self._previous_length > len(bar_string):
            print(f'\r{" "*self._previous_length}', end='')
        print(bar_string, end='')
        self._previous_length = len(bar_string)

    def _end(self):
        '''
        Finalizes the display of the loading bar by showing the completed state.
        '''
        percent_filled = self.value / self.max_value
        filled_cells = round(self.length * percent_filled)
        bar_string = '\r'
        if self.show_progress:
            bar_string += f'[{self.value}{" " * (len(str(self.max_value))-len(str(self.value)))}/{self.max_value}]  '
        if self.show_percentage:
            bar_string += f'[{round(percent_filled * 100)}{"  " if percent_filled<0.1 else " " if percent_filled<1 else ""}%]  '
        bar_string += f'[{self.filled * filled_cells}{self.empty * (self.length-filled_cells)}]'
        print(f'\r{" "*self._previous_length}', end='')
        print(bar_string)
