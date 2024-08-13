SRC_DIR := raw
DEST_DIR := anonymized
LOG_DIR := log
VENV_PATH = ~/.venv/anonymize-gpx

$(shell mkdir -p $(DEST_DIR))
$(shell rm -rf $(LOG_DIR)/*)

FILES := $(wildcard $(SRC_DIR)/*)
TARGETS := $(FILES:$(SRC_DIR)/%=$(DEST_DIR)/%)

all: venv install $(TARGETS)

venv:
	python3 -m venv $(VENV_PATH)

install: venv
	source $(VENV_PATH)/bin/activate && \
	pip install --disable-pip-version-check -q -r requirements.txt

FORCE:

$(DEST_DIR)/%: $(SRC_DIR)/% FORCE
	source $(VENV_PATH)/bin/activate && \
	FILE_ID=$$(jot -r 1 1 100000000); \
	export FILE_ID && \
	cat $< | \
	python3 scripts/remove-metadata.py | \
	python3 scripts/adjust-accuracy.py | \
	python3 scripts/simplify.py | \
	python3 scripts/format-xml.py > $@

clean:
	rm -f $(DEST_DIR)/*
	rm -f $(DEST_DIR)/*

.PHONY: all venv install clean
