USER=postgres
# SE TIVER SENHA, DESCOMENTE A PRÓXIMA LINHA
#HAS_PASSWORD=-W
NO_DEBUG=--quiet

all:
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/scheme.pgsql
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/triggers.pgsql
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/popular_banco.pgsql
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/views.pgsql



.PHONY:
clear:
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "DROP DATABASE deliverydb"
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM user_delivery"
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "DROP USER admin_delivery, user_delivery"
