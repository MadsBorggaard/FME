# FME

Forskellige workflows til FME

-- Matrikel.zip

Workflow til at hente matrikeldata fra Datafordeleren
Der skal indsættes et brugernavn og password til en tjenestebruger fra Datafordeleren
og der skal sætte en boundingbox med min_x, min_y, max_x og max_y

Workflowet looper alle lag igennem med den første bbox, hvis den rammer mere end 10000 elementer, så bliver boxen delt, og den prøver igen
dette gør den indtil den er under 10000 elementer.

Alle features bliver gemt i en fil-geodatabase
Alle bboxe bliver gemt i shape-filer, så man kan se hvor mange der bliver hentet i hver bbox.

Schemaet til Matriklen er lavet i hånden, så det skal tilpasses hvis der kommer ændringer i schemaet fra Datafordeleren.

-- BBR Kommune Udtræk.zip

Henter BBR data fra Datafordeleren og indlæser dem i database
HUSK AT SÆTTE KOMMUNEKODE PÅ FIL-DOWNLOAD FRA DATAFORDELEREN NÅR DEN OPRETTES.
Det tager ca. 25-30 minutter at hente BBR data for Lemvig Kommune.
