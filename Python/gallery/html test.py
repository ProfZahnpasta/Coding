import os
path = "D:\Eigene Dateien\Schule\Fächer\Informatik Berk\Python\gallery\img"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")

print(dir_list)



html = """
<html>
    <head>
        <title></title>


        <style>
            img {
                width: 400px;
                height: 300px;
                object-fit: cover;
            }
        </style>
    </head>
    <body>
        <h1>Meine Bildergallerie</h1>
        Dies sind tolle Fotos!
"""

for f in dir_list:
     html += '<img src="img/' + f + '">'

html += """
    </body>
</html>
"""



print (html)
with open("index.html", "w") as file:
    file.write(html)