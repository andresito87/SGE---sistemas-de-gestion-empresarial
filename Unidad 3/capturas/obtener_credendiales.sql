CREATE OR REPLACE FUNCTION obtener_credenciales(p_user_id INT)
RETURNS TABLE(login VARCHAR, password VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT u.login, u.password
    FROM public.res_users u
    WHERE u.id = p_user_id;
END;
$$ LANGUAGE plpgsql;

SELECT public.get_user_credentials(2);


