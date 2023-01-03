from conan import ConanFile
from conan import tools
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
from conan.tools.build import check_min_cppstd
import os, re

def get_version():
    try:
        with open("CMakeLists.txt", encoding='utf8') as cmkfile:
            content = cmkfile.read()
            version_major = re.search("set\(\$\{PRJ_PREFIX\}_VERSION_MAJOR (.*)\)", content).group(1)
            version_minor = re.search("set\(\$\{PRJ_PREFIX\}_VERSION_MINOR (.*)\)", content).group(1)
            version_patch = re.search("set\(\$\{PRJ_PREFIX\}_VERSION_PATCH (.*)\)", content).group(1)
            return (version_major + "." + version_minor + "." + version_patch).strip()
    except:
        return None

class mytestRecipe(ConanFile):
    name = "mytest"
    version = get_version()

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of spf-utils package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "test/*"

    def requirements(self):
        self.requires("gtest/1.12.1", build=True, test=True)

    def validate(self):
        check_min_cppstd(self, "17")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["mytest"]
