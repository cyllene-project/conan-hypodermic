from conans import ConanFile, CMake, tools


class HypodermicConan(ConanFile):
    name = "hypodermic"
    version = "2.4"
    license = "MIT"
    url = "https://github/cyllene-project/conan-hypodermic"
    description = "Hypodermic is an IoC container for C++. It provides dependency injection to your existing design."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "*"
    requires = "boost_test/1.65.1@bincrafters/stable", "boost_signals2/1.65.1@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/ybainier/Hypodermic.git")
        self.run("cd Hypodermic && git checkout v2.4")

    def package(self):
        pass

    def package_id(self):
        self.info.header_only()


    def package_info(self):
        self.copy("*.h", dst="include/Hypodermic", src="Hypodermic/Hypodermic")

    def configure(self):
        self.options["Boost"].header_only = True
