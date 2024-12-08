CREATE OR REPLACE FUNCTION create_bills()
   RETURNS TRIGGER
AS
$$
BEGIN
    INSERT INTO spending_spend(money, category_id, user_id)
    VALUES (0, 0, NEW.id);
    INSERT INTO wallet_wallet(cash, card, deposit, user_id)
    VALUES (0, 0, 0, NEW.id);

   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER registration
    AFTER INSERT ON auth_user
    FOR EACH ROW
    EXECUTE FUNCTION create_bills();