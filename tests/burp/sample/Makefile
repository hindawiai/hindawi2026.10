CFLAGS = -O2 -DVALUE=40 -DLIMIT=2
prog: src/main.c src/lib.c src/lib.h
	$(CC) $(CFLAGS) -Isrc -o prog src/main.c src/lib.c
