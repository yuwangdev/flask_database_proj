# DROP DATABASE IF EXISTS ERMS;
# CREATE DATABASE IF NOT EXISTS ERMS;
USE ERMS;

# User Table
DROP TABLE IF EXISTS Usertable;
CREATE TABLE IF NOT EXISTS Usertable (
  username     VARCHAR(255) NOT NULL,
  nameInfo     VARCHAR(255) NOT NULL,
  passwordInfo VARCHAR(255) NOT NULL,
  PRIMARY KEY (username)
);

# Municipalities Table
DROP TABLE IF EXISTS Municipalities;
CREATE TABLE IF NOT EXISTS Municipalities (
  username       VARCHAR(255) NOT NULL,
  populationSize INT          NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username)
  REFERENCES Usertable (username)
);

# GovernmentAgencies Table
DROP TABLE IF EXISTS GovernmentAgencies;
CREATE TABLE IF NOT EXISTS GovernmentAgencies (
  username     VARCHAR(255) NOT NULL,
  jurisdiction VARCHAR(255) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username)
  REFERENCES Usertable (username)
);

# Company Table
DROP TABLE IF EXISTS Company;
CREATE TABLE IF NOT EXISTS Company (
  username      VARCHAR(255) NOT NULL,
  headquarteres VARCHAR(255) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username)
  REFERENCES Usertable (username)
);

# Individuals Table
DROP TABLE IF EXISTS Individuals;
CREATE TABLE IF NOT EXISTS Individuals (
  username    VARCHAR(255) NOT NULL,
  jobTitle    VARCHAR(255) NOT NULL,
  dateOfHired DATE         NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (username)
  REFERENCES Usertable (username)
);

# Incident Table
DROP TABLE IF EXISTS Incident;
CREATE TABLE IF NOT EXISTS Incident (
  IncidentID   INT          NOT NULL,
  IncidentDate DATE         NOT NULL,
  Description  VARCHAR(255) NOT NULL,
  Latitude     FLOAT(10, 6) NOT NULL,
  Longitude    FLOAT(10, 6) NOT NULL,
  username     VARCHAR(255) NOT NULL,
  PRIMARY KEY (IncidentID),
  FOREIGN KEY (username)
  REFERENCES Usertable (username)
);

# ESF Table
DROP TABLE IF EXISTS ESF;
CREATE TABLE IF NOT EXISTS ESF (
  EsfID INT          NOT NULL,
  item  VARCHAR(255) NOT NULL,
  PRIMARY KEY (EsfID)
);

# intert values into ESF table
INSERT ESF
(EsfID, item)
VALUES
  (1, 'Transportation'),
  (2, 'Communic cation'),
  (3, 'Public Works and Engineering'),
  (4, 'Firefighting'),
  (5, 'Emergency Management'),
  (6, 'Mass Care Emergenct Assitance,Housing,and Human Services'),
  (7, 'Logistics Management and Resource Support'),
  (8, 'Public Health and Medical Services'),
  (9, 'Search and Rescue'),
  (10, 'Oil and Hazardous Materials Response'),
  (11, 'Agriculture and Natural Resources'),
  (12, 'Energy'),
  (13, 'Public Safety and Security'),
  (14, 'Long-Term Community Recovery'),
  (15, 'External Affairs');

# CostUnit Table
DROP TABLE IF EXISTS CostUnit;
CREATE TABLE IF NOT EXISTS CostUnit (
  CostUnit VARCHAR(255) NOT NULL,
  PRIMARY KEY (CostUnit)
);

# Resource Table
DROP TABLE IF EXISTS Resource;
CREATE TABLE IF NOT EXISTS Resource (
  ResourceID    INT          NOT NULL,
  ResourceName  VARCHAR(255) NOT NULL,
  model         VARCHAR(255),
  CurrentStatus VARCHAR(255) NOT NULL,
  Latitude      FLOAT(10, 6) NOT NULL,
  Longitude     FLOAT(10, 6) NOT NULL,
  `Owner`       VARCHAR(255) NOT NULL,
  CostPerValue  NUMERIC      NOT NULL,
  EsfID         INT          NOT NULL,
  CostUnit      VARCHAR(255) NOT NULL,
  CurrentUser   VARCHAR(255),
  StartDate     DATE,
  DueDate       DATE,
  PRIMARY KEY (ResourceID),
  FOREIGN KEY (`Owner`)
  REFERENCES Usertable (username),
  FOREIGN KEY (EsfID)
  REFERENCES ESF (EsfID),
  FOREIGN KEY (CurrentUser)
  REFERENCES Usertable (username),
  FOREIGN KEY (CostUnit)
  REFERENCES CostUnit (CostUnit)
);

# SearchResource Table
DROP TABLE IF EXISTS SearchResource;
CREATE TABLE IF NOT EXISTS SearchResource (
  ResourceID INT NOT NULL,
  IncidentID INT NOT NULL,
  PRIMARY KEY (ResourceID, IncidentID),
  FOREIGN KEY (ResourceID)
  REFERENCES Resource (ResourceID),
  FOREIGN KEY (IncidentID)
  REFERENCES Incident (IncidentID)
);

# ResourceRequest Table
DROP TABLE IF EXISTS ResourceRequest;
CREATE TABLE IF NOT EXISTS ResourceRequest (
  IncidentID         INT  NOT NULL,
  RequestID          INT  NOT NULL,
  ExpectedReturnDate DATE NOT NULL,
  ResourceID         INT  NOT NULL,
  PRIMARY KEY (IncidentID, RequestID),
  FOREIGN KEY (ResourceID)
  REFERENCES Resource (ResourceID),
  FOREIGN KEY (IncidentID)
  REFERENCES Incident (IncidentID)
);

# Capability Table
DROP TABLE IF EXISTS Capability;
CREATE TABLE IF NOT EXISTS Capability (
  ResourceID     INT          NOT NULL,
  CapabilitiyStr VARCHAR(255) NOT NULL,
  PRIMARY KEY (ResourceID, CapabilitiyStr),
  FOREIGN KEY (ResourceID)
  REFERENCES Resource (ResourceID)
);

# Additional Table
DROP TABLE IF EXISTS Additional;
CREATE TABLE IF NOT EXISTS Additional (
  ResourceID INT NOT NULL,
  EsfID      INT NOT NULL,
  PRIMARY KEY (ResourceID, EsfID),
  FOREIGN KEY (ResourceID)
  REFERENCES Resource (ResourceID),
  FOREIGN KEY (EsfID)
  REFERENCES ESF (EsfID)

);

# Repair Table
DROP TABLE IF EXISTS RepairResource;
CREATE TABLE IF NOT EXISTS RepairResource (
  ResourceID INT          NOT NULL,
  repairID   INT          NOT NULL,
  username   VARCHAR(255) NOT NULL,
  startDate  DATE         NOT NULL,
  endDate    DATE         NOT NULL,

  PRIMARY KEY (ResourceID, repairID),
  FOREIGN KEY (username)
  REFERENCES Usertable (username),
  FOREIGN KEY (ResourceID)
  REFERENCES Resource (ResourceID)
);

