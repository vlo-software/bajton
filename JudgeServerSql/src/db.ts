import initSqlJs from "sql.js";

export interface Test {
  id: number;
  userQuery: string;
  testQuery: string;
}

export interface TestResult {
  id: number;
  testOutput: string;
  userOutput: string;
  result: "passed" | "failed" | "error";
}

export const runTests = async (
  database: string,
  tests: Array<Test>
): Promise<Array<TestResult>> => {
  const results = await Promise.all(
    tests.map(async (test): Promise<TestResult> => {
      try {
        const userOutput = await getOutput(database, test.userQuery);
        const testOutput = await getOutput(database, test.testQuery);
        const result =
          userOutput[userOutput.length - 1].values.join(", ") ===
          testOutput[testOutput.length - 1].values.join(", ");
        return {
          id: test.id,
          testOutput: testOutput[testOutput.length - 1].values.join(", "),
          userOutput: userOutput[userOutput.length - 1].values.join(", "),
          result: result ? "passed" : "failed",
        };
      } catch (_) {
        return {
          id: test.id,
          testOutput: "",
          userOutput: "",
          result: "error",
        };
      }
    })
  );
  return results;
};

const getOutput = async (database: string, query: string) => {
  const db = await loadDatabase(database);
  return db.exec(Buffer.from(query, "base64").toString("utf8"));
};

const loadDatabase = async (database: string) => {
  const sql = await initSqlJs();
  const db = new sql.Database();
  db.run(Buffer.from(database, "base64").toString("utf8"));
  return db;
};
