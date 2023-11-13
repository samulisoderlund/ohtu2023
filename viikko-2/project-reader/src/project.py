class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _bulletify(self, list):
        return "\n".join("- " + s for s in list) if len(list) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license or '-'}\n"
            "\n"
            f"Authors:\n{self._bulletify(self.authors)}\n"
            "\n"
            f"Dependencies:\n{self._bulletify(self.dependencies)}\n"
            "\n"
            f"Development dependencies:\n{self._bulletify(self.dev_dependencies)}"
        )
