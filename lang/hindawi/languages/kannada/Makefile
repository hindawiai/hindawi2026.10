#Copyright (C) 2026 Abhishek Choudhary
#Makefile for Hindawi kannada — structure matches guru/Makefile

FLEX ?= $(or $(shell command -v flex 2>/dev/null),/tmp/flexroot/usr/bin/flex)
FLIB ?= -L/tmp/flexroot/usr/lib/x86_64-linux-gnu -lfl
ROMENAGRI ?= /tmp/chintamani/Romenagri

all: h2c c2h

h2c: h2c.uhin
	cat h2c.uhin | iconv -f utf-8 -t utf-16 | $(ROMENAGRI)/uni2acii | $(ROMENAGRI)/acii2cf > h2c.lex
	$(FLEX) -o lexyy.c -8 h2c.lex
	gcc -o h2c lexyy.c $(FLIB)

c2h: c2h.uhin
	cat c2h.uhin | iconv -f utf-8 -t utf-16 | $(ROMENAGRI)/uni2acii | $(ROMENAGRI)/acii2cf > c2h.lex
	$(FLEX) -o lexyy.c -8 c2h.lex
	gcc -o c2h lexyy.c $(FLIB)

clean:
	rm -f h2c c2h lexyy.c h2c.lex c2h.lex

clean_all: clean

install:
	@echo "install target: copy h2c c2h to EXECDIR"

uninstall:
	@echo "uninstall target: remove from EXECDIR"
