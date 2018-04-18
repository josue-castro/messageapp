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
  pid INTEGER REFERENCES Person(pid) NOT NULL, --send by
  gid INTEGER REFERENCES GroupChat(gid) NOT NULL, --send to
  numLikes INTEGER,
  numDislikes INTEGER,
  replying INTEGER REFERENCES Messages(mid), --original message
  date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE Members(
  gid INTEGER REFERENCES GroupChat(gid) NOT NULL,
  pid INTEGER REFERENCES Person(pid) NOT NULL,
  numMembers INTEGER,
  PRIMARY KEY (gid, pid)
);

CREATE TABLE Contacts(
  pid INTEGER REFERENCES Person(pid) NOT NULL, --user id that adds contact
  contact_name VARCHAR(30) NOT NULL,
  phone CHAR REFERENCES Person(phone),
  email VARCHAR REFERENCES Person(email),
  contact_id INTEGER REFERENCES Person(pid), --user id to be added
  PRIMARY KEY (pid, contact_id),
  CHECK (phone IS NOT NULL OR email IS NOT NULL)
);

CREATE TABLE Likes(
  mid INTEGER REFERENCES Messages(mid),
  pid INTEGER REFERENCES Person(pid),
  PRIMARY KEY (mid, pid)
);

CREATE TABLE Dislikes(
  mid INTEGER REFERENCES Messages(mid),
  pid INTEGER REFERENCES Person(pid),
  PRIMARY KEY (mid, pid)
);
