test:
	python3 -m unittest -v test_partida

clean:
	rm -rf *.pyc __pycache__

# invocar esta regla así: make commit msg="Mensaje para el commit"
commit:
	echo git pull
	echo git add *.py Makefile
	echo git commit -m "$(msg)"
	echo git push
