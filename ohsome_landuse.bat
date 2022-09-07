curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=forest or landuse=grass or landuse=greenfield) and (geometry:polygon)" ^
-o 2018_Nature.geojson ^
"https://api.ohsome.org/v1/elements/geometry"

curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=farmland or landuse=meadow or landuse=orchard or landuse=vineyard or landuse=greenhouse_horticulture or landuse=plant_nursery) and (geometry:polygon)" ^
-o 2018_Agriculture.geojson ^
"https://api.ohsome.org/v1/elements/geometry"

curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=allotments or landuse=flowerbed or landuse=cemetery or landuse=village_green) and (geometry:polygon)" ^
-o 2018_UrbanVegetation.geojson ^
"https://api.ohsome.org/v1/elements/geometry"

curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=aquaculture or landuse=basin or landuse=reservoir or landuse=salt_pond) and (geometry:polygon)" ^
-o 2018_Water.geojson ^
"https://api.ohsome.org/v1/elements/geometry"

curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=commercial or landuse=residential or landuse=recreation_ground) and (geometry:polygon)" ^
-o 2018_SemiVegetation.geojson ^
"https://api.ohsome.org/v1/elements/geometry"

curl -X POST ^
--data-urlencode "bboxes=8.573690501677584,49.351977127610745,8.793906378285733,49.45965586843265" ^
--data-urlencode "time=2018-12-31" ^
--data-urlencode "filter=(landuse=construction or landuse=education or landuse=industrial or landuse=retail or landuse=brownfield or landuse=depot or landuse=garages or landuse=landfill or landuse=military or landuse=port or landuse=quarry or landuse=railway) and (geometry:polygon)" ^
-o 2018_NonVegetation.geojson ^
"https://api.ohsome.org/v1/elements/geometry"
