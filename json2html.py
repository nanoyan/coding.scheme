from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

config = GenerationConfiguration(copy_css=False,template_md_options=md)

generate_from_filename("response.schema.json", "index4.md", config=config)


# # Delete footer
# with open('templates/coding-schema-temp.html') as currentfile, open('templates/coding-schema.html','w') as nf:
#     atFooter = None

#     for line in currentfile:
#         if "</footer>" in line:
#              line.replace(line,'')
#              atFooter = False
#         elif "<footer>" in line or atFooter :
#             line.replace(line,'')
#             atFooter = True
#         else :
#             nf.write(line)

# pathlib.Path.unlink('templates/coding-schema-temp.html')

