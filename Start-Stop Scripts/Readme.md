<h1>Startup Python Script:</h1>
<p>Opretter en txt-fil med et uuid</p>

<h1>Shutdown Python Script:</h1>
Skriver forskelligt statestik omkring kørslen af workflowet, bl.a. om det har kørt ok eller ej.<br>
Der bliver skrevet følgende information i databasen:<br>
<ul><li>dato: datoen og tidspunktet for hvornår scriptet har kørt</li>
<li>id: uuid'en fra Startup Python Script</li>
<li>name: navnet på workflowet, man kan jo navngive alle sine workflows med samme navn, derfor også uuid</li>
<li>status: er workflowet kørt ok eller fejlet</li>
<li>elapsedRunTime: Den faktiske forløbne tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.</li>
<li>cpuSysTime: Mængden af system -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.</li>
<li>cpuUserTime: Mængden af bruger -CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.</li>
<li>cpuTime: Den samlede CPU -tid i sekunder fra lige før FME_BEGIN_PYTHON -scriptet blev kaldt til lige før FME_END_PYTHON -scriptet blev kaldt.</li>
<li>failureMessage: Fejlmeddelelsen, hvis kørslen mislykkedes, tom hvis kørslen lykkedes.</li>
<li>featuresRead: En Python-dictionary, indekseret efter featuretype, som indeholder antallet af læste features for denne featuretype. (virker ikke med FeatureReader transformer)</li>
<li>featuresWritten: En Python-dictionary, indekseret efter featuretype, som indeholder antallet af skrevne features for denne featuretype. (virker ikke med FeatureReader transformer)</li>
<li>totalFeaturesRead: Det samlede antal læste features. (virker ikke med FeatureReader transformer)</li>
<li>totalFeaturesWritten: Det samlede antal skrevne features. (virker ikke med FeatureReader transformer)</li></ul>
<h1>FME_Statestik.sql</h1>
Dette er en sql fil der opretter tabellen der henvises til i Shutdown Python Script<br>
Navnet på tabellen kan selvfølgelig ændres, så skal det også bare gøres i Shutdown Python Script
<h1>ToDo</h1>
<ul><li>Lave så Shutdown Python Script også sender en mail når der er fejl</li>
</ul>
