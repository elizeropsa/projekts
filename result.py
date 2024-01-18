import PyPDF2
from pathlib import Path

jsumma=0
jatlikums=70
jpapildus_atlikums=25
jpapildus_summa=0
dsumma=0
datlikums=70
dpapildus_atlikums=25
dpapildus_summa=0

pdf_cels = "invoices/"
pdf_files = [file for file in Path(pdf_cels).glob("*.pdf")]
for pdf_path in pdf_files:
    with open (pdf_path, "rb") as file:
        pdf_reader=PyPDF2.PdfReader(file)
        lapu_sk=len(pdf_reader.pages)
        lapa = pdf_reader.pages[0]
        text = lapa.extract_text()

        pos1 = text.find('Veikals "Maxima"')
        pos2 = text.find("Kase Nr.")
        adrese = (text[pos1+17:pos2-19].rstrip())
       
        pos3 = text.find("KOPĀ:")
        pos4 = text.find("Autorizācijas Nr")
        if pos3 != -1 and pos4 != -1:
            cena = (text[pos3+30:pos4-4].rstrip())
            cena = cena.replace(",",".")
            cena = float(cena)

        pos5 = text.find("LAIKS")
        pos6 = text.find("Visa")
        laiks = (text[pos5+19:pos5+27].rstrip())


        if laiks == "2024- 01":
            if adrese == "Matīsa iela 23" or adrese == "Lidoņu iela 30a":
                jsumma = jsumma + cena
                jatlikums = jatlikums - cena
            if adrese == "Valmieras iela 17a,":
                jpapildus_summa = jpapildus_summa + cena
                jpapildus_atlikums = jpapildus_atlikums - cena
    


        if laiks == "2023- 12":
            if adrese == "Matīsa iela 23" or adrese == "Lidoņu iela 30a":
                dsumma = dsumma + cena
                datlikums = datlikums - cena
            if adrese == "Valmieras iela 17a,":
                dpapildus_summa = dpapildus_summa + cena
                dpapildus_atlikums = dpapildus_atlikums - cena


print(f"Decembrī pārtikā iztērētā naudas summa: {dsumma} EUR")
print(f"Decembrī papildus iztērētā naudas summa: {dpapildus_summa} EUR")
if (datlikums + dpapildus_atlikums > 0):
    print(f"Decembrī tev pāri palika {round(datlikums+dpapildus_atlikums, 2)} EUR")
else: 
    print("Decembrī tu iztērēji visu savu mēneša limitu!!")

print("\n")

print(f"Janvārī pārtikā iztērētā summa: {jsumma} EUR")
print(f"Janvārī papildus iztērētā summa: {jpapildus_summa} EUR")

if jatlikums + jpapildus_atlikums > 0:
    print(f"Janvārī atlikusī pārtikai paredzētā summa: {round(jatlikums, 2)} EUR")
    print(f"Papildus tēriņiem janvārī atlikusī summa: {round(jpapildus_atlikums, 2)} EUR")
if (datlikums + dpapildus_atlikums > 0):
        print(f"Janvārī tev pieejamā naudas summa (ieskaitot decembra atlikumu) ir {round(jatlikums+jpapildus_atlikums+datlikums+dpapildus_atlikums, 2)} EUR")
else: 
    print("UZMANĪBU!!! Tu esi iztērējusi visu mēneša limitu!!!!")
        
