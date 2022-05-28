all:
	@echo "Compilación y ejecución de la práctica"
	python3 serv3.py &
	python3 cli3.py prueba.txt
	pkill -f serv3.py
	@echo "Terminado"

binary:
	@echo "Compilación y ejecución de la práctica con fichero /boot/vmlinuz.old"
	python3 serv3.py &
	python3 cli3.py /boot/vmlinuz
	pkill -f serv3.py
	@echo "Terminado"

services:
	@echo "Compilación y ejecución de la práctica con fichero /etc/services"
	python3 serv3.py &
	python3 cli3.py /etc/services
	pkill -f serv3.py
	@echo "Terminado"

clean:
	@echo "Limpiando..."
	rm /tmp/ped5_p3_app1*
