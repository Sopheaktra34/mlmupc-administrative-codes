/* =================================================================================
   DATABASE: MLMUPC
   PURPOSE : Cambodia Administrative Boundaries
   LEVELS  : Province → District → Commune → Village
   CHARSET : utf8mb4 (Khmer safe)
   ENGINE  : InnoDB
================================================================================= */

CREATE DATABASE IF NOT EXISTS mlmupc
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE mlmupc;

-- Provinces
CREATE TABLE provinces (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    name_kh VARCHAR(150) NOT NULL,
    name_en VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Districts
CREATE TABLE districts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    province_id INT NOT NULL,
    code VARCHAR(10) NOT NULL UNIQUE,
    name_kh VARCHAR(150) NOT NULL,
    name_en VARCHAR(150),
    district_type ENUM('Srok','Krong','Khan') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_district_province
        FOREIGN KEY (province_id)
        REFERENCES provinces(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Communes
CREATE TABLE communes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    district_id INT NOT NULL,
    code VARCHAR(10) NOT NULL UNIQUE,
    name_kh VARCHAR(150) NOT NULL,
    name_en VARCHAR(150),
    commune_type ENUM('Commune','Sangkat') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_commune_district
        FOREIGN KEY (district_id)
        REFERENCES districts(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Villages
CREATE TABLE villages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    commune_id INT NOT NULL,
    code VARCHAR(15) NOT NULL UNIQUE,
    name_kh VARCHAR(150) NOT NULL,
    name_en VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_village_commune
        FOREIGN KEY (commune_id)
        REFERENCES communes(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB;