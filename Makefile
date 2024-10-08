SRC_DIR := $(shell echo ~/gitRepo/gpx-data/data/strava)
DEST_DIR := anonymized
LOG_DIR := log
VENV_PATH = ~/.venv/anonymize-gpx

FILES := $(wildcard $(SRC_DIR)/*.gpx)
TARGETS := $(FILES:$(SRC_DIR)/%=$(DEST_DIR)/%)

all: venv install $(TARGETS)

venv:
	@python3 -m venv $(VENV_PATH)

install: venv
	@source $(VENV_PATH)/bin/activate && \
	pip install --disable-pip-version-check -q -r requirements.txt

$(DEST_DIR)/%.gpx: $(SRC_DIR)/%.gpx
	@source $(VENV_PATH)/bin/activate && \
	if python3 scripts/is-allowed.py $<; then \
		echo "Processing: "$<; \
		cat $< | \
		python3 scripts/remove-metadata.py | \
		python3 scripts/adjust-accuracy.py $@ | \
		python3 scripts/trim.py $@ | \
		python3 scripts/simplify.py $@ | \
		python3 scripts/format-xml.py > $@; \
	else \
		echo "Skipping: "$<; \
	fi

maps:
	source $(VENV_PATH)/bin/activate && \
	python3 scripts/make-maps.py anonymized

clean:
	rm -f $(DEST_DIR)/*
	rm -rf $(LOG_DIR)/*

.PHONY: all venv install clean maps
