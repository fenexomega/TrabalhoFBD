\c deliverydb

GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_delivery;
GRANT USAGE ON SCHEMA public to user_delivery;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO user_delivery;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_delivery;

GRANT ALL ON ALL TABLES IN SCHEMA public TO admin_delivery;
GRANT USAGE ON SCHEMA public to admin_delivery;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO admin_delivery;
GRANT ALL ON ALL TABLES IN SCHEMA public TO admin_delivery;
