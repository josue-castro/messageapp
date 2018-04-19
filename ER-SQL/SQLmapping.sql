CREATE TABLE Person(
  pid BIGSERIAL PRIMARY KEY,
  firstName VARCHAR(20) NOT NULL,
  lastName VARCHAR(30) NOT NULL,
  username VARCHAR(20) UNIQUE NOT NULL,
  phone CHAR(10) UNIQUE,
  email VARCHAR(50) UNIQUE,
  CHECK (phone IS NOT NULL or email IS NOT NULL)
);

CREATE TABLE GroupChat(
  gid BIGSERIAL PRIMARY KEY,
  gName VARCHAR(30) NOT NULL,
  pid BIGINT REFERENCES Person(pid) --administrator id
);

CREATE TABLE Messages(
  mid BIGSERIAL PRIMARY KEY,
  content VARCHAR(280),
  pid BIGINT REFERENCES Person(pid), --send by
  gid BIGINT REFERENCES GroupChat(gid), --send to
  date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE Hashtag(
  hid BIGSERIAL PRIMARY KEY,
  tag VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE Members(
  gid BIGINT REFERENCES GroupChat(gid),
  pid BIGINT REFERENCES Person(pid),
  PRIMARY KEY (gid, pid)
);

CREATE TABLE Contacts(
  pid BIGINT REFERENCES Person(pid), --user id that adds contact
  contact_id BIGINT REFERENCES Person(pid), --user id to be added
  PRIMARY KEY (pid, contact_id)
);

CREATE TABLE Likes(
  mid BIGINT REFERENCES Messages(mid),
  pid BIGINT REFERENCES Person(pid),
  PRIMARY KEY (mid, pid)
);

CREATE TABLE Dislikes(
  mid BIGINT REFERENCES Messages(mid),
  pid BIGINT REFERENCES Person(pid),
  PRIMARY KEY (mid, pid)
);

CREATE TABLE Tagged(
  mid BIGINT REFERENCES Messages(mid),
  hid BIGINT REFERENCES Hashtag(hid),
  PRIMARY KEY (mid, hid)
);

CREATE TABLE Replies(
  mid BIGINT REFERENCES Messages(mid), --original message
  reply_id BIGINT REFERENCES Messages (mid), --reply message
  PRIMARY KEY (mid, reply_id)
);