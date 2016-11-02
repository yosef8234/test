all: inject payload host
inject: code_inject.o
	gcc -g code_inject.o -o inject
code_inject.o: code_inject.c
	gcc -c code_inject.c
payload:
	gcc -fpic -pie -nostdlib payload.c -o payload
host:
	gcc host.c -o host
	@echo "Now run ./host &; ./inject `pidof host` ./payload"
clean:
	rm -f *.o payload host
