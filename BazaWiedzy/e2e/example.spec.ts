import { test, expect } from "@playwright/test";

test("should navigate to the dashboard page", async ({ page }) => {
  // Start from the index page (the baseURL is set via the webServer in the playwright.config.ts)
  await page.goto("/bw");
  // Find an element with the text 'About Page' and click on it
  await page.click("text=Dashboard");
  // The new URL should be "/about" (baseURL is used there)
  await expect(page).toHaveURL("/bw/dashboard");
  // The new page should contain an h1 with "About Page"
  await expect(page.locator("h1")).toContainText("Dashboard");
});
