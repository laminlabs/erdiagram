from IPython.display import SVG, display


def view(pdot):
    try:
        plt = SVG(pdot.create_svg())
        display(plt)
    except FileNotFoundError:
        raise RuntimeError(
            "Visualizing a diagram requires graphviz. "
            "Install, e.g., via sudo apt-get -y install graphviz."
        )
