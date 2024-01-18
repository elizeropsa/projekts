Cik naudas man šomēnes vēl atlicis?

Programmas apraksts

Ikdienā saskaros ar jautājumiem "Cik naudas man šomēnes vēl ir? Vai man pietiks pārtikai? Vai pietiks biļetei uz mājām? ", tāpēc nolēmu izveidot programmu, kas, analizējot uz e-pastu atsūtītos Maximas čekus PDF formātā, aprēķina gan jau manis iztērēto naudu, gan atlikušo, ja esmu iztērējusi visu naudu, tiek izvadīts attiecīgs paziņojums. Šo programmu iespējams izmantot jebkurā mēneša dienā, tā analizē gan tieši pārtikai paredzēto naudas summu, gan papildus tēriņiem paredzēto. Šī programma apskata 3 dažādu lokāciju Maxima veikalus. Divi no tiem atrodas Rīgā, tātad tur tērēju pārtikai paredzēto naudu, un viens atrodas Cēsīs - tur tiek tērēta papildus tēriņu nauda. Manis izveidotā programma lieliski tiek galā ar visām šīm lokācijām. Tiek apskatīti arī dažādi mēneši. Konkrēti šajā programmā tie ir decembris un janvāris. Programmas rezultātā  tiek izvadīts, cik daudz naudas es decembrī iztērēju pārtikai un cik daudz papildus tēriņos, cik daudz naudas man decembrī palika pāri (ja tika iztērēts viss budžets, izvada attiecīgu paziņojumu), cik daudz naudas esmu janvārī iztērējusi pārtikai, cik papildus tēriņos, cik daudz naudas man vēl atlicis pārtikai, cik citiem tēriņiem, un atsevišķi tiek izvadīts paziņojums par atlikušo mēneša budžetu pārtikai kopā ar papildus tēriņiem, pieskaitot klāt vēl decembra atlikumu, ja tāds ir bijis. 

Izmantotās Python bibliotēkas

PyPDF2

PyPDF2 bibliotēku izmantoju vispārīgam darbam ar PDF failiem. Ar šīs bibliotēkas palīdzību izveidoju objektu, kas nolasa katru PDF failu, no kura vēlāk izgūstu tekstu, ko vēlāk varu apstrādāt programmas vajadzībām.

Pathlib

No pathlib bibliotēkas izmantoju klasi Path. Manā programmā šī bibliotēka un klase tiek izmantota, lai nodrošinātu visu PDF failu apstrādi. Sākumā norādu ceļu uz visiem PDF failiem, pēctam ar Path palīdzību iegūstu visus ceļus uz norādītajā mapē esošajiem failiem, kas atbilst '.pdf' paplašinājumam.
