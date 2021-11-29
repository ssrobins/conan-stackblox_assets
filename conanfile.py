from conans import ConanFile

class Conan(ConanFile):
    name = "stackblox_assets"
    version = "1.0.0"
    description = "StackBlox assets"
    license = "MIT"
    url = f"https://github.com/ssrobins/conan-{name}"
    revision_mode = "scm"
    exports = "*"
    build_policy = "missing"

    def package(self):
        self.copy("*", excludes=("conan.py", "conanbuildinfo.txt"))
