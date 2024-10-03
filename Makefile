.PHONY: all
all:
	make -C lab7-recv all
	make -C lab7-send all

.PHONY: upload
upload:
	make -C lab7-recv upload
	make -C lab7-send upload

.PHONY: recv
recv:
	python recv.py

.PHONY: send
send:
	python send.py
