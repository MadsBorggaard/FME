# Startup Python Script:
Opretter en txt-fil med et uuid

# Shutdown Python Script - statestik til sql:
***Der skal være installeret pyodbc i python for at dette virker***\
Skriver forskelligt statestik omkring kørslen af workflowet, bl.a. om det har kørt ok eller ej.\
Der bliver skrevet følgende information i databasen:
- **dato:** datoen og tidspunktet for hvornår scriptet har kørt
- **id:** uuid'en fra Startup Python Script
- **name:** navnet på workflowet, man kan jo navngive alle sine workflows med samme navn, derfor også uuid
- **status:** er workflowet kørt ok eller fejlet
- **elapsedRunTime:** Den faktiske forløbne tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.
- **cpuSysTime:** Mængden af system -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.
- **cpuUserTime:** Mængden af bruger -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.
- **cpuTime:** Den samlede CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.
- **failureMessage:** Fejlmeddelelsen, hvis kørslen mislykkedes, tom hvis kørslen lykkedes.
- **featuresRead:** En Python-dictionary, indekseret efter featuretype, som indeholder antallet af læste features for denne featuretype. (virker ikke med FeatureReader transformer)
- **featuresWritten:** En Python-dictionary, indekseret efter featuretype, som indeholder antallet af skrevne features for denne featuretype. (virker ikke med FeatureReader transformer)
- **totalFeaturesRead:** Det samlede antal læste features. (virker ikke med FeatureReader transformer)
- **totalFeaturesWritten:** Det samlede antal skrevne features. (virker ikke med FeatureReader transformer)
# FME_Statestik.sql
Dette er en sql fil der opretter tabellen der henvises til i Shutdown Python Script\
Navnet på tabellen kan selvfølgelig ændres, så skal det også bare gøres i Shutdown Python Script
# Shutdown Python Script - send log mail from gmail:
***Der skal oprettes et app password hvis man har aktiveret 2trins login til gmail***\
Der skal oplyses følgende i scriptet:
- afsender email
- modtager email
- gmail brugernavn (det samme som afsender email)
- gmail password (app password hvis man har 2trins login)
# Startup Pyton Script - csv-fil
Opretter en csv-fil til statestik
# Shutdown Python Script - statestik til csv
Gemmer statestik til csv-fil samme sted som FME workspacet er gemt, det er samme oplysninger som gemmes hvis man bruger *Shutdown Python Script - statestik til sql*\
**SKAL BRUGE Startup Python Script - csv-fil**
# Ekstra
Man kan selvfølgelig tilføje mere til mailen, f.eks. hvor lang tid den kørte m.m.\
og man kan selvfølgelig sætte dem sammen, så den både gemmer i sql og sender en mail

