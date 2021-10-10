from typing import Callable
import random

class EmailBlock:

    def uniform_density(i: float):
        return 1.

    def __init__(self, lines: int, char_width: int, text: str, density_function: Callable = uniform_density):
        self.lines = lines
        self.density_function = density_function
        self.text = text

        if len(text) > char_width / 2:
            raise ValueError('Text is too big for the line width')

        # Calculate max density
        self.max_density = (char_width / 2.) // len(text)

    def render(self) -> str:
        for line in self.lines:

            progress = line / self.lines
            density = self.density_function (progress)

            nb_text = density * self.max_density
            nb_gaps = nb_text - 1

            random.sample(range(0, 1000), nb_gaps)


nb_gaps = 4
print(random.sample(range(0, 1000), nb_gaps))
