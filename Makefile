USER=postgres
# SE TIVER SENHA, DESCOMENTE A PRÓXIMA LINHA
#HAS_PASSWORD=-W
NO_DEBUG=--quiet
PARAMS=$(NO_DEBUG) $(HAS_PASSWORD)
FEITO=@echo -e "\e[1;32mFeito\e[0m"
PRINT=@printf "\e[1m"; printf


all:
	@echo -e "\e[1mUsuário: \e[1;31m $(USER)\e[0m"
	@echo -e "\e[1mParametros passados: \e[0m-U $(USER) $(HAS_PASSWORD) $(NO_DEBUG)  "
	$(PRINT) "Criando esquema....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/scheme.pgsql
	$(FEITO)
	$(PRINT) "Criando triggers e storaged procedures....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/triggers.pgsql
	$(FEITO)
	$(PRINT) "Populando banco....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/popular_banco.pgsql
	$(FEITO)
	$(PRINT) "Criando views....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/views.pgsql
	$(FEITO)
	$(PRINT) "Gerenciando permissões....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) < pgscripts/permissoes.pgsql
	$(FEITO)



.PHONY:
clear:
	$(PRINT) "Limpando tudo....."
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "DROP DATABASE deliverydb"
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM user_delivery"
	@psql -U $(USER) $(HAS_PASSWORD) $(NO_DEBUG) -c "DROP USER admin_delivery, user_delivery"
	$(FEITO)
