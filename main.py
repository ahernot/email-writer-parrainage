
from writer import Email, EmailBlock

if __name__ == '__main__':

    email = Email (blocks=[
        {
            'text':'A',
            'nb_lines': 40,
            'max_density': 10,
            'density_function': EmailBlock.squared_density
        },
        {
            'text':'B',
            'nb_lines': 20,
            'max_density': 10,
            'density_function': EmailBlock.uniform_density
        },
        {
            'text':'C',
            'nb_lines': 20,
            'max_density': 10,
            'density_function': EmailBlock.uniform_density
        },
        {
            'text':'D',
            'nb_lines': 20,
            'max_density': 10,
            'density_function': EmailBlock.uniform_density
        },
        {
            'text':'E',
            'nb_lines': 20,
            'max_density': 10,
            'density_function': EmailBlock.uniform_density
        },
        {
            'text':'F',
            'nb_lines': 40,
            'max_density': 15,
            'density_function': EmailBlock.uniform_density
        }
    ], page_width=200)

    with open('out.html', 'w', encoding='utf-8') as html_output:
        html_output.write('<div style="white-space: pre-wrap; font-size: 16pt; line-height: 400%;">')
        html_output.write (email.render())
        html_output.write('</div>')
