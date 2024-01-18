from conans import ConanFile


class NlohmannJsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.11.3"
    license = "MIT"
    url = "https://github.com/nlohmann/json"

    def source(self):
        self.run(
            f"git clone --single-branch --branch v{self.version} --depth 1 https://github.com/nlohmann/json.git src"
        )

    def package(self):
        self.copy("*.hpp", dst="include", src="src/include")
        self.copy("*.h", dst="include", src="src/include")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
