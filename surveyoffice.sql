BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "daily" (
	"id"	INTEGER NOT NULL UNIQUE,
	"user_id"	INTEGER,
	"equipment_id"	INTEGER,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES ""
);
CREATE TABLE IF NOT EXISTS "equipment" (
	"id"	INTEGER NOT NULL UNIQUE,
	"type"	TEXT,
	"serial_no"	TEXT,
	"assigned_to_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("assigned_to_id") REFERENCES "user"("id")
);
CREATE TABLE IF NOT EXISTS "maintenance" (
	"id"	INTEGER NOT NULL UNIQUE,
	"equipment_id"	INTEGER,
	"date"	TEXT,
	"calibration"	INTEGER COLLATE BINARY,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("equipment_id") REFERENCES ""
);
CREATE TABLE IF NOT EXISTS "roll" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "time_log" (
	"id"	INTEGER NOT NULL UNIQUE,
	"job_no"	TEXT,
	"start_time"	TEXT,
	"end_time"	TEXT,
	"work_description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"roll_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
