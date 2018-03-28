CREATE TABLE Person(
  pid SERIAL PRIMARY KEY,
  firstName VARCHAR(20) NOT NULL,
  lastName VARCHAR(30) NOT NULL,
  username VARCHAR(20) UNIQUE NOT NULL,
  phone CHAR(10) UNIQUE,
  email VARCHAR(50) UNIQUE,
  CHECK (phone IS NOT NULL or email IS NOT NULL)
);

CREATE TABLE GroupChat(
  gid SERIAL PRIMARY KEY,
  gName VARCHAR(30) NOT NULL,
  admin INTEGER REFERENCES Person(pid) NOT NULL
);

CREATE TABLE Messages(
  mid SERIAL PRIMARY KEY,
  content VARCHAR(280),
  sendBy INTEGER REFERENCES Person(pid) NOT NULL,
  sendTo INTEGER REFERENCES GroupChat(gid) NOT NULL,
  replied INTEGER REFERENCES Messages(mid),
  date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE Members(
  "group" INTEGER REFERENCES GroupChat(gid) NOT NULL,
  "user" INTEGER REFERENCES Person(pid) NOT NULL,
  PRIMARY KEY ("group","user")
);

CREATE TABLE Contacts(
  main_user INTEGER REFERENCES Person(pid) NOT NULL,
  contact_name VARCHAR(30) NOT NULL,
  contact_phone CHAR REFERENCES Person(phone),
  contact_email VARCHAR REFERENCES Person(email),
  contact_id INTEGER REFERENCES Person(pid),
  PRIMARY KEY (main_user, contact_id),
  CHECK (contact_phone IS NOT NULL OR contact_email IS NOT NULL)
);
