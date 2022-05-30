from IPython.display import SVG, display


def view(pdot):
    plt = SVG(pdot.create_svg())
    display(plt)
