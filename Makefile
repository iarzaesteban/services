up:
	xhost +"local:docker@";
	docker-compose --profile service up;

dbshell:
	docker exec -it postgres-db psql -U postgres -d servicesdatabase

# Parar los servicios
down:
	docker-compose down

# Reconstruir la imagen del frontend
rebuild-frontend:
	docker-compose up --build react-frontend

# Reconstruir la imagen del backend
rebuild-backend:
	docker-compose up --build django-backend

# Reconstruir la imagen de la base de datos
rebuild-db:
	docker-compose up --build postgres-db

# Limpiar los volúmenes y reiniciar todo
clean:
	docker-compose down -v
	docker-compose up --build

# Comando general para reconstruir todos los servicios
rebuild-all:
	docker-compose up --build