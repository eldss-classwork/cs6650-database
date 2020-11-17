-- Creates the schema for a ski resort lift rides database.
-- author: Evan Douglass

-- Drop tables
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS Skiers;
DROP TABLE IF EXISTS Resorts;
DROP TABLE IF EXISTS Lifts;
DROP TABLE IF EXISTS LiftRides;
SET FOREIGN_KEY_CHECKS=1;

-- Create tables
CREATE TABLE Skiers (
    skierID INT PRIMARY KEY
);

CREATE TABLE Resorts (
    resortID VARCHAR(40) PRIMARY KEY
);

CREATE TABLE Lifts (
    liftNum INT NOT NULL,
    resortID VARCHAR(40) NOT NULL,
    vertical INT,
    PRIMARY KEY (liftNum, resortID),
    FOREIGN KEY (resortID) REFERENCES Resorts(resortID)
);

CREATE TABLE LiftRides (
    skierID INT NOT NULL,
    liftNum INT NOT NULL,
    resortID VARCHAR(40) NOT NULL,
    `day` INT NOT NULL,
    `time` INT NOT NULL,
    PRIMARY KEY (skierID, liftNum, resortID, `day`, `time`),
    FOREIGN KEY (skierID) REFERENCES Skiers(skierID),
    FOREIGN KEY (liftNum, resortID) REFERENCES Lifts(liftNum, resortID)
);