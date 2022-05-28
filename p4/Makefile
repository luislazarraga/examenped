all:
	@echo "Compilación y ejecución de la práctica"
	python3 serv4.py &
	sleep 1
	python3 cli4.py prueba.txt
	pkill -f serv4.py
	@echo "Terminado"

services:
	@echo "Compilación y ejecución de la práctica"
	python3 serv4.py &
	sleep 1
	python3 cli4.py /etc/services
	pkill -f serv4.py
	@echo "Terminado"

binary:
	@echo "Compilación y ejecución de la práctica"
	python3 serv4.py &
	sleep 1
	python3 cli4.py /boot/vmlinuz
	pkill -f serv4.py
	@echo "Terminado"

clean:
	@echo "Limpiando..."
