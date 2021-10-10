from typing import Callable
import random

class EmailBlock:

    def uniform_density(i: float):
        return 1.

    def __init__(self, lines: int, page_width: int, text: str, density_function: Callable = uniform_density):
        self.lines = lines
        self.density_function = density_function
        self.text = text
        self.text_width = len(self.text)

        # Raise error if text too big for width of page
        if len(text) > page_width / 2:
            raise ValueError('Text is too big for the line width')

        # Calculate max density
        self.max_density = (page_width / 2.) // self.text_width



    def render(self) -> str:
        for line in self.lines:

            progress = line / self.lines
            density = self.density_function (progress)

            nb_text = density * self.max_density
            nb_gaps = nb_text - 1

            available_gap = self.page_width - (self.text_width * nb_text)

            random.sample(range(0, 1000), nb_gaps)


nb_gaps = 4
print(random.sample(range(0, 1000), nb_gaps))
