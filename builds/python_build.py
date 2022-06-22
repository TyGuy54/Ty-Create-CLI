# useful note
# control d makes it so ypu can edit all of the same variable names

import os, yaml, sys
import shutil
from rich.console import Console

class Build:
    def __init__(self, prj_name):
        self.prj_name = prj_name
        self.home_path = os.path.expanduser('~/Desktop/')


    def build_project(self):
        console = Console()

        # open the python yaml file
        with open("python_package.yaml", "r") as rf:
            conf = yaml.load(rf, Loader=yaml.Loader)

        build_dir = conf["build_dir"]
        project_name = build_dir.replace(conf["build_dir"], self.prj_name)

        if os.path.exists(project_name):
            console.print(f"Project {self.prj_name} Already Exsist", style="red")
            sys.exit(1)
        else:
            console.print(f"Created Project {self.prj_name} at {self.home_path}", style="green")
        

        for target in conf['boilerplate_location']:
            src = target['source_location']
            tar = os.path.join(project_name, src)
            des = self.home_path+tar

            # check os
            if sys.platform == "linux" or sys.platform == "linux2":
                # linux
                os.makedirs(self.home_path+project_name)
                shutil.copytree(src, des)
            if sys.platform == "darwin":
                # OS X
                os.makedirs(self.home_path+project_name)
                shutil.copytree(src, des)
            if sys.platform == "win32":
                # Windows
                os.makedirs(self.home_path+project_name)
                shutil.copytree(src, des)


        os.chdir(self.home_path+project_name)

