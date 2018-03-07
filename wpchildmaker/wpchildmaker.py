import jinja2
import sys
import os

theme_name = sys.argv[1]
customer_name = sys.argv[2]
customer_site = sys.argv[3]


def make_child(name=theme_name, customer=customer_name, site=customer_site):
    env = jinja2.Environment()
    env.loader = jinja2.FileSystemLoader("templates/")
    template_footer = env.get_template("footer.php")
    template_functions = env.get_template("functions.php")
    template_style = env.get_template("style.css")

    child_path = "mychilds/" + theme_name + "/"
    directory = os.path.dirname(child_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    f_footer = open('mychilds/' + theme_name + '/' + 'footer.php', 'w')
    f_footer.write(template_footer.render(customer_name=customer_name))

    f_functions = open('mychilds/' + theme_name + '/' + 'functions.php', 'w')
    f_functions.write(template_functions.render(customer_site=customer_site))

    f_style = open('mychilds/' + theme_name + '/' + 'style.css', 'w')
    f_style.write(template_style.render(theme_name=theme_name))


if __name__ == '__main__':
    make_child()
