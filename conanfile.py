from conans import ConanFile, CMake, tools
import os

class CpptomlConan(ConanFile):
    name = "cpptoml"
    version = "0.1.0"
    license = "MIT"
    url = "https://github/cyllene-project/conan-cpptoml"
    description = "cpptoml is a header-only library for parsing TOML"
    settings = None
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/skystrife/cpptoml.git")

    def build(self):
        pass
        
    def package(self):
        self.copy("*.h", dst="include", src=os.path.join("cpptoml", "include"))
        
    def package_info(self):
        self.info.header_only()

