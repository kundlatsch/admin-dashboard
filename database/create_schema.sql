CREATE TABLE Users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) NOT NULL,
    name varchar(255),
    password_hash varchar(255) NOT NULL,
    is_admin bool
);

CREATE TABLE Clients (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    date_of_birth varchar(255),
    cpf varchar(255),
    rg varchar(255),
    rg_state varchar(255),
    phone_number varchar(255)
);
