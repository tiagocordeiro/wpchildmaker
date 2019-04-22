import os
import shutil
import sys
from zipfile import ZipFile

import click
import jinja2
from halo import Halo


@click.command()
@click.option("--theme_name", prompt="Child theme name", help="Não use espaço ou caracteres especiais")
@click.option("--customer_name", prompt="Customer name", help="Nome do cliente")
@click.option("--customer_site", prompt="url do site", help="ex. https://www.mulhergorila.com")
@click.option("--template", prompt="Template name", help="ex. Divi", default="Divi")
def make_child(theme_name, customer_name, customer_site, template):
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()

    pathname = os.path.dirname(sys.argv[0])
    template_dir = os.path.abspath(pathname) + "/templates/" + template
    template_files = os.listdir(template_dir)
    env = jinja2.Environment()
    env.loader = jinja2.FileSystemLoader(template_dir)

    child_path = os.path.abspath(pathname) + "/mychilds/" + theme_name + "/"
    directory = os.path.dirname(child_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    for file in template_files:
        if file.endswith(".jpg") or file.endswith(".png"):
            shutil.copy2(template_dir + "/" + file, directory)
            spinner.succeed("Arquivo " + file + " Copiado")
        else:
            template_file = env.get_template(file)
            template_writer = open("mychilds/" + theme_name + "/" + file, "w")
            template_writer.write(template_file.render(theme_name=theme_name,
                                                       customer_name=customer_name,
                                                       customer_site=customer_site, ))
            spinner.succeed("Arquivo " + file + " Gerado")

    spinner.succeed("Arquivos gerados.")
    ziparchive(theme_name)
    spinner.stop()


def ziparchive(theme_name):
    # initializing empty file paths list
    file_paths = []
    os.chdir("./mychilds/")
    spinner_zip = Halo(text="Compactando arquivos", spinner="dots")

    # crawling through directory and subdirectories
    for root, directories, files in os.walk("./" + theme_name + "/"):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # printing the list of all files to be zipped
    spinner_zip.info("Following files will be zipped:")
    for file_name in file_paths:
        spinner_zip.succeed("Arquivo" + file_name + " OK")

    # writing files to a zipfile
    with ZipFile("./" + theme_name + ".zip", "w") as filezip:
        # writing each file one by one
        for file in file_paths:
            filezip.write(file)

    spinner_zip.succeed("All files zipped successfully!")


if __name__ == "__main__":
    make_child()
