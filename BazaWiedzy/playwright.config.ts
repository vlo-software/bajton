import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "e2e",
  use: {
    /* Base URL to use in actions like `await page.goto('/')`. */
    baseURL: "http://oj-backend:8000",
  },
});
