import { createClient } from "redis";
import { runTests } from "./db";

(async () => {
  const client = createClient({
    url: `redis://${
      process.env.NODE_ENV === "production" ? "oj-redis" : "localhost"
    }:6379`,
  });

  client.on("error", (err) => console.log("Redis Client Error", err));

  await client.connect();

  const subscriber = client.duplicate();

  await subscriber.connect();

  await subscriber.subscribe("judge-server-sql-jobs", async (message) => {
    const data = JSON.parse(message); // { submissionId, database, tests }
    const results = await runTests(data.database, data.tests);
    const response = JSON.stringify({
      submissionId: data.submissionId,
      results,
    });
    await client.lPush("judge-server-sql-results", response);
  });
})();
