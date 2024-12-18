import spacy
import os
import re
from datetime import datetime
import tkinter as tk 
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

nlp = spacy.load('nb_core_news_lg')
elp = spacy.load('en_core_web_sm')

land = ["Afghanistan", "Albania", "Algerie", "Andorra", "Angola", "Antigua og Barbuda", "Argentina", "Armenia", "Australia", "Østerrike", "Aserbajdsjan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Hviterussland", "Belgia", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia og Hercegovina", "Botswana", "Brasil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Kambodsja", "Kamerun", "Canada", "Kapp Verde", "Den sentralafrikanske republikk", "Tsjad", "Chile", "Kina", "Colombia", "Komorene", "Republikken Kongo", "Den demokratiske republikken Kongo", "Costa Rica", "Elfenbenskysten", "Kroatia", "Cuba", "Kypros", "Tsjekkia", "Danmark", "Djibouti", "Dominica", "Den dominikanske republikk", "Øst-Timor", "Ecuador", "Egypt", "El Salvador", "Ekvatorial-Guinea", "Eritrea", "England", "Estland", "Etiopia", "Fiji", "Finland", "Frankrike", "Gabon", "Gambia", "Georgia", "Tyskland", "Ghana", "Hellas", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Ungarn", "Island", "India", "Indonesia", "Iran", "Irak", "Irland", "Israel", "Italia", "Jamaica", "Japan", "Jordan", "Kasakhstan", "Kenya", "Kiribati", "Nord-Korea", "Sør-Korea", "Kosovo", "Kuwait", "Kirgisistan", "Laos", "Latvia", "Libanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Litauen", "Luxembourg", "Makedonia", "Madagaskar", "Malawi", "Malaysia", "Maldivene", "Mali", "Malta", "Marshalløyene", "Mauritania", "Mauritius", "Mexico", "Mikronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Marokko", "Mosambik", "Myanmar", "Namibia", "Nauru", "Nepal", "Nederland", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norge", "Oman", "Pakistan", "Palau", "Panama", "Papua Ny-Guinea", "Paraguay", "Peru", "Filippinene", "Polen", "Portugal", "Qatar", "Romania", "Russland", "Rwanda", "Saint Kitts og Nevis", "Saint Lucia", "Saint Vincent og Grenadinene", "Samoa", "San Marino", "São Tomé og Príncipe", "Saudi-Arabia", "Senegal", "Serbia", "Seychellene", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Salomonøyene", "Somalia", "Sør-Afrika", "Sør-Sudan", "Spania", "Sri Lanka", "Sudan", "Surinam", "Swaziland", "Sverige", "Sveits", "Syria", "Taiwan", "Tadsjikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad og Tobago", "Tunisia", "Tyrkia", "Turkmenistan", "Tuvalu", "Uganda", "Ukraina", "De forente arabiske emirater", "Storbritannia", "USA", "Uruguay", "Usbekistan", "Vanuatu", "Vatikanstaten", "Venezuela", "Vietnam", "Jemen", "Zambia", "Zimbabwe"]

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Republic of the Congo", "Democratic Republic of the Congo", "Costa Rica", "Ivory Coast", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "England", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "North Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Eswatini", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "USA", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]

Fregion = ["beach", "park", "forest", "lake", "river", "mountain", "desert", "island", "valley"]

# Finder informasjon fra filene. Eksempler er Land, Region og senderens navn.
def extract_info(file_content):
    doc = nlp(file_content)
    for ent in doc.ents:
        if ent.label_ == 'PER' and '-' not in ent.text and '_' not in ent.text:
            name = ent.text
            break
        else:
            name = "Unknown"
    country = "Unknown"
    region = "Unknown"

    print("Entities found:")
    for ent in doc.ents:
        print(f"Text: {ent.text}, Label: {ent.label_}")

    for ent in doc.ents:
        if ent.label_ == "GPE_LOC":
            if ent.text.lower() in [c.lower() for c in land]:
                country = ent.text
            elif country != 'Unknown' and region == 'Unknown' and 'beach' not in ent.text.lower():
                region = ent.text
    if country == 'Unknown':
        doc2 = elp(file_content)
        for ent in doc2.ents:
            if ent.label_ == "GPE_LOC":
                if ent.text.lower() in [c.lower() for c in countries]:
                    country = ent.text
                elif country != 'Unknown' and region == 'Unknown' and 'beach' not in ent.text.lower():
                    region = ent.text
    if name == 'Unknown':
        doc2 = elp(file_content)
        for ent in doc2.ents:
            if ent.label_ == 'PER' and '-' not in ent.text and '_' not in ent.text:
                name = ent.text
                break
            else:
                name = "Unknown"
                
    origin = f'{country}.{region}' if region != 'Unknown' else country

    return name, origin, country

# Gir filen et nytt navn. Dermed lagrer den filen i den riktige folderen basert på hvilket land filen er fra ifølge filens inhold.
def process_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()

    name, origin, country = extract_info(file_content)

    new_filename = f"{name}_{origin}"

    project_folder = os.path.dirname(os.path.abspath(__file__))
    target_directory = os.path.join(project_folder, 'Mail', country)
    os.makedirs(target_directory, exist_ok=True)
    new_file_path = os.path.join(target_directory, new_filename)

    with open(file_path, 'a') as f:
        f.write('\n\nOriginal navn: {navn}'.format(navn=str(file_path)))
    
    try:
        end = f"{new_file_path}.txt"
        os.rename(file_path, end)
    except FileExistsError:
        retry = f"{new_file_path}-copy.txt"
        os.rename(file_path, retry)

    print(f"File moved and renamed to: {new_file_path}")

# Før den prosseserer en fil vil den sjekke om det er en folder. Hvis det er en folder vil den ta ut alle text document filenen i folderen og sortere dem individuelt.
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_file(file_path)

# Denne tar å utfører de andre prossesene når en fil eller folder blir droppet oppi boksen.
def drop(event):
    path = event.data.strip('{}')
    if os.path.isdir(path):
        process_folder(path)
    elif os.path.isfile(path) and path.endswith('.txt'):
        process_file(path)
    else:
        print("Error: Invalid file type or path.")
        print(f"Path: {path}")
        print("Solve: Please drop a .txt file or a folder containing .txt files.")

# Her blir størrelsen og titelen på app vinduet definert.
root = TkinterDnD.Tk()
root.title("Text file drop box.")
root.geometry("400x300")

# Her bestemmer jeg hva vinduet skal være/gjøre. Her har jeg bestemt at vinduet skal være en drop boks.
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()