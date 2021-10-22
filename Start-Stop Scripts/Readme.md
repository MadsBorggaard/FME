<h1>Startup Python Script:</h1>
<p>Opretter en txt-fil med et uuid</p>

<h1>Shutdown Python Script:</h1>
Skriver forskelligt statestik omkring kørslen af workflowet, bl.a. om det har kørt ok eller ej.<br>
Der bliver skrevet følgende information i databasen:<br>
dato: datoen og tidspunktet for hvornår scriptet har kørt<br>
id: uuid'en fra Startup Python Script<br>
name: navnet på workflowet, man kan jo navngive alle sine workflows med samme navn, derfor også uuid<br>
status: er workflowet kørt ok eller fejlet
elapsedRunTime: Den faktiske forløbne tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.<br>
cpuSysTime: Mængden af system -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.<br>
cpuUserTime: Mængden af bruger -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.<br>
cpuTime: Den samlede CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.<br>
failureMessage: Fejlmeddelelsen, hvis kørslen mislykkedes, tom hvis kørslen lykkedes.<br>
featuresRead: En Python-dictionary, indekseret efter featuretype, som indeholder antallet af læste features for denne featuretype. (virker ikke med FeatureReader transformer)<br>
featuresWritten: En Python-dictionary, indekseret efter featuretype, som indeholder antallet af skrevne features for denne featuretype. (virker ikke med FeatureReader transformer)<br>
totalFeaturesRead: Det samlede antal læste features. (virker ikke med FeatureReader transformer)<br>
totalFeaturesWritten: Det samlede antal skrevne features. (virker ikke med FeatureReader transformer)<br>
