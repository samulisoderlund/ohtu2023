from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        project = toml.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            project["tool"]["poetry"]["name"],
            project["tool"]["poetry"]["description"],
            project["tool"]["poetry"]["license"],
            project["tool"]["poetry"]["authors"],
            project["tool"]["poetry"]["dependencies"].keys(),
            project["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()
        )
