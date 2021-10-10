import random

def random_hex_color() -> str:
    """
    Generate a random hexadecimal color value.
    :return: Random hexadecimal color value
    """
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class Style:

    @classmethod
    def random(cls):
        return Style (
            random_hex_color(),
            random_hex_color(),
            bool(random.getrandbits(1)),
            bool(random.getrandbits(1))
        )

    def __init__(self, text_color: str, background_color: str, bold: bool, underline: bool):
        
        style_list = list()

        # Build style list
        style_list.append ('color: {};' .format(text_color))
        style_list.append ('background-color: {};' .format(background_color))
        if bold: style_list.append ('font-weight: bold;')
        if underline: style_list.append ('text-decoration: underline;')

        # Create style string
        style_string = ' ' .join(style_list)
        self.html_string = '<span style="{style}">{text}</span>' .format(**{
            'style': style_string,
            'text': '{text}'
        })

    def __repr__(self):
        return self.html_string
