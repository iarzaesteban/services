-- Creación de las tablas de la base de datos
CREATE EXTENSION IF NOT EXISTS postgis;
-- Users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    mail VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    avatar VARCHAR(255),
    description TEXT,
    social_networks JSONB,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_status BOOLEAN DEFAULT TRUE,
    last_activity_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    address GEOGRAPHY(POINT),
    UNIQUE (mail)
);

-- Clients
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Imágenes de trabajos
CREATE TABLE IF NOT EXISTS work_images (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    url_image VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolution VARCHAR(20)
);

-- Chats
CREATE TABLE IF NOT EXISTS chats (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    client_id INT REFERENCES clients(id) ON DELETE CASCADE,
    message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    multimedia VARCHAR(255),
    type VARCHAR(20) CHECK(tipo IN ('text', 'image', 'video')),
    deletion_date TIMESTAMP,
    state BOOLEAN DEFAULT TRUE
);

-- Calificaciones
CREATE TABLE IF NOT EXISTS qualifications (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    client_id INT REFERENCES clients(id) ON DELETE CASCADE,
    punctuation INT CHECK(punctuation BETWEEN 1 AND 5),
    comment TEXT,
    comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    edition_date TIMESTAMP
);
