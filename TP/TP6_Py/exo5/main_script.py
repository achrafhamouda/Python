import xml.etree.ElementTree as ET

#Dabaord on lit le fichier
tree = ET.parse("C:/Users/achra/Desktop/exo5/students.xml")
root = tree.getroot()

# Puis on affichage les etudiants
for student in root.findall("student"):
    name = student.find("name").text
    grade = student.find("grade").text
    print(f"Nom : {name}, Note : {grade}")

#Apres on ajout un nv etd
nv_etudiant = ET.Element("student")

nom = ET.SubElement(nv_etudiant, "name")
nom.text = "achraf"

note = ET.SubElement(nv_etudiant, "grade")
note.text = "20"

# ici on met un nouvel etd a la fin de la liste
root.append(nv_etudiant)

# Sauvegarde
tree.write("C:/Users/achra/Desktop/exo5/students.xml", encoding="utf-8", xml_declaration=True)

