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
    date_of_birth varchar(255) NOT NULL,
    cpf varchar(255) NOT NULL,
    rg varchar(255) NOT NULL,
    rg_state varchar(255) NOT NULL,
    phone_number varchar(255) NOT NULL
);

CREATE TABLE Adresses (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    address varchar(255) NOT NULL,
    complement varchar(255),
    city varchar(255),
    state varchar(255),
    client_id int,
    FOREIGN KEY (client_id) REFERENCES Clients(id)
);
