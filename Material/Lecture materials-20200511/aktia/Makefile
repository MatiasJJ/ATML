RACES := 1 2 3 4 5
RACEFILES := $(addsuffix .race.csv,$(RACES))

ZIPFILES := Makefile join.py parsefile.py fmi_to_weather.py fmi.csv readme.txt aktia.csv weather.csv aktia10K.ipynb

.PHONY: all
all: weather.csv aktia.csv

aktia.zip: $(ZIPFILES)
	rm -f aktia.zip && zip aktia.zip $(ZIPFILES)

aktia.csv: $(RACEFILES)
	python join.py $(RACES)
	
weather.csv: fmi.csv
	python fmi_to_weather.py

.PHONY: raw
raw: $(RAWFILES)

5.race.csv:
	# URL for race 5 looks different
	python parsefile.py --race 5 --url "https://www.kokkens.fi/kilpailut/2018/aktia/index.php?action=show&sarja=10KM"

%.race.csv:
	python parsefile.py --race $*

.PHONY: clean
clean:
	rm -f $(RACEFILES)
	
.PHONY: cleanall
cleanall: clean
	rm -f aktia.zip aktia.csv weather.csv
