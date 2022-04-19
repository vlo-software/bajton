import { runTests } from "../src/db";

const database = Buffer.from(
  `
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT,
	password TEXT,
	email TEXT,
	role TEXT
);

INSERT INTO users (username, password, email, role) VALUES ('admin', 'password1', 'example@example.com', 'admin');
INSERT INTO users (username, password, email, role) VALUES ('frog-master-83', 'password1', 'example@example.com', 'admin');
INSERT INTO users (username, password, email, role) VALUES ('julia', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('dave', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('robert', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('jane', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('harry', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('anne', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('john', 'password1', 'example@example.com', 'user');
INSERT INTO users (username, password, email, role) VALUES ('emy', 'password1', 'example@example.com', 'user');
`
).toString("base64");

const toBase64 = (str: string) => Buffer.from(str).toString("base64");

describe("testing db.ts", () => {
  test("Correct answers should be graded positively", async () => {
    const tests = [
      {
        id: 1,
        userQuery: toBase64("SELECT * FROM users"),
        testQuery: toBase64("SELECT * FROM users"),
      },
      {
        id: 2,
        userQuery: toBase64("SELECT * FROM users WHERE id = 1"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 1"),
      },
      {
        id: 3,
        userQuery: toBase64("SELECT * FROM users WHERE id > 3"),
        testQuery: toBase64("SELECT * FROM users WHERE id > 3"),
      },
    ];
    expect(
      (await runTests(database, tests)).map(({ result }) => result)
    ).toEqual(["passed", "passed", "passed"]);
  });
  test("Wrong answers should be graded negatively", async () => {
    const tests = [
      {
        id: 1,
        userQuery: toBase64("SELECT * FROM users"),
        testQuery: toBase64("SELECT username FROM users"),
      },
      {
        id: 2,
        userQuery: toBase64("SELECT * FROM users WHERE id = 1"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 2"),
      },
      {
        id: 3,
        userQuery: toBase64("SELECT * FROM users WHERE id > 3"),
        testQuery: toBase64("SELECT * FROM users WHERE id < 3"),
      },
    ];
    expect(
      (await runTests(database, tests)).map(({ result }) => result)
    ).toEqual(["failed", "failed", "failed"]);
  });
  test("Errors should be graded with an error", async () => {
    const tests = [
      {
        id: 1,
        userQuery: toBase64("SELECT * FROM users ŁER id = 1"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 1"),
      },
      {
        id: 2,
        userQuery: toBase64("SELECT * FROM userz WHERE id = 2"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 2"),
      },
      {
        id: 3,
        userQuery: toBase64("dexter"),
        testQuery: toBase64("SELECT * FROM users WHERE id < 3"),
      },
    ];
    expect(
      (await runTests(database, tests)).map(({ result }) => result)
    ).toEqual(["error", "error", "error"]);
  });
  test("Mixed results should be handled correctly", async () => {
    const tests = [
      {
        id: 1,
        userQuery: toBase64("SELECT * FROM users"),
        testQuery: toBase64("SELECT * FROM users"),
      },
      {
        id: 2,
        userQuery: toBase64("SELECT * FROM users WHERE id = 1"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 2"),
      },
      {
        id: 3,
        userQuery: toBase64("what's the meaning of life?"),
        testQuery: toBase64("SELECT * FROM users WHERE id > 3"),
      },
    ];
    expect(
      (await runTests(database, tests)).map(({ result }) => result)
    ).toEqual(["passed", "failed", "error"]);
  });
  test("Semicolon at the end shouldn't influence the results", async () => {
    const tests = [
      {
        id: 1,
        userQuery: toBase64("SELECT * FROM users;"),
        testQuery: toBase64("SELECT * FROM users"),
      },
      {
        id: 2,
        userQuery: toBase64("SELECT * FROM users WHERE id = 1;"),
        testQuery: toBase64("SELECT * FROM users WHERE id = 2"),
      },
      {
        id: 3,
        userQuery: toBase64("what's the meaning of life?;"),
        testQuery: toBase64("SELECT * FROM users WHERE id > 3"),
      },
    ];
    expect(
      (await runTests(database, tests)).map(({ result }) => result)
    ).toEqual(["passed", "failed", "error"]);
  });
});
