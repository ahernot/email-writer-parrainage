from typing import Callable
import math
import numpy

from preferences import *


class EmailBlock:

    def uniform_density(i: float): return 1.
    def squared_density(i: float): return i**2

    def __init__(self, nb_lines: int, page_width: int, text: str, max_density: int = 10, density_function: Callable = uniform_density):
        # Unpack and process input
        self.nb_lines = nb_lines
        self.page_width = page_width
        self.text = text
        self.text_width = len(self.text)
        self.density_function = density_function

        # Raise error if text too big for width of page
        if len(text) > page_width / 2:
            raise ValueError('Text is too big for the line width')

        # Calculate max density
        self.max_density = min(max_density, (page_width / 2.) // self.text_width)



    def render(self) -> str:

        lines = list()
        for line_id in range(self.nb_lines):

            line = str()
            # Calculate density
            progress = line_id / self.nb_lines
            density = self.density_function (progress)

            # Calculate number of strings in line
            nb_text = max(1, math.ceil(density * self.max_density))
            nb_gaps = max(1, nb_text) #first gap

            # Calculate available single gap
            available_gap = (self.page_width - (self.text_width * nb_text)) / nb_gaps
            random_gaps = numpy.random.rand(nb_gaps)
            random_gaps_scaled = random_gaps * available_gap * 2  # *2 because the average random gap is 0.5 before scaling

            # Generate line
            for text_id in range(nb_text):
                line += CHAR_BREAK * math.ceil(random_gaps_scaled[text_id])
                line += self.text

            lines.append(line)
        
        return LINE_BREAK.join(lines)
            



eb = EmailBlock (100, 200, 'B', density_function=EmailBlock.squared_density)
eb.render()


