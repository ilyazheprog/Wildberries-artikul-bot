all:
	@docker compose up -d --build

build:
	@docker compose build
	
down:
	@docker compose down

logs:
	@docker compose logs bot -f

bash:
	@docker compose exec -it bot bash

db_login:
	# \l - list databases
	# \c database - connect to db
	# \dt - list tables
	# select * from table - view table content
	@docker compose exec db psql --username=wb --dbname=wb

db_clear:
	# remove all data from database, including user data
	@ docker compose exec bot bash -c "pdm db-clear"

alembic_migration:
	@ docker compose exec back bash -c "pdm alembic-migration \"$(name)\""


alembic_upgrade:
	@ docker compose exec back bash -c "pdm alembic-upgrade"
alembic_downgrade:
	@ docker compose exec back bash -c "pdm alembic-downgrade"
seeders:
	@docker compose exec -it bot bash -c "pdm apply-seeds"

lint:
	pdm isort
	pdm black