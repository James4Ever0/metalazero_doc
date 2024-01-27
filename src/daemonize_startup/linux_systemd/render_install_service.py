import jinja2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d","--description",type=str,default="trivial_service")
parser.add_argument("-s","--script",type=str,required=True)
parser.add_argument("-n","--name",type=str,required=True)
parser.add_argument("-e","--execute",action="store_true")

args = parser.parse_args()
execute = args.execute
desc = args.description
script = args.script
name = args.name

def get_template(file_name):
    with open(file_name,"r") as f:
        content = f.read()
        template = jinja2.Template(content)
        return template

def render_template(file_name,dic):
    return get_template(file_name).render(dic)

def save_render_template(file_name, data, outfile):
    with open(outfile,"w+") as f:
        f.write(render_template(file_name, data))

if __name__ == "__main__":
    service_file = name + ".service"
    execute_script_file = "script.sh"
    save_render_template("template.j2", {"service_description": desc, "service_script": script}, service_file)
    save_render_template("routine.j2", {"service": name, "service_file": service_file}, execute_script_file)
    if execute:
        os.system("bash {}".format(execute_script_file))
