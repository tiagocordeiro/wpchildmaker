from zipfile import ZipFile
import jinja2
import click
import os


@click.command()
@click.option('--theme_name', prompt='Child theme name',
              help='Não use espaço ou caracteres especiais')
@click.option('--customer_name', prompt='Customer name',
              help='Nome do cliente')
@click.option('--customer_site', prompt='url do site',
              help='ex. https://www.mulhergorila.com')
def make_child(theme_name, customer_name, customer_site):
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
    f_footer.close()

    f_functions = open('mychilds/' + theme_name + '/' + 'functions.php', 'w')
    f_functions.write(template_functions.render(customer_site=customer_site))
    f_functions.close()

    f_style = open('mychilds/' + theme_name + '/' + 'style.css', 'w')
    f_style.write(template_style.render(theme_name=theme_name))
    f_style.close()

    ziparchive(theme_name)


def ziparchive(theme_name):
    # initializing empty file paths list
    file_paths = []
    os.chdir('./mychilds/')

    # crawling through directory and subdirectories
    for root, directories, files in os.walk('./' + theme_name + '/'):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile('./' + theme_name + '.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')


if __name__ == '__main__':
    make_child()
