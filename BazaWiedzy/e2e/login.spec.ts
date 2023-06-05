import { test, expect } from "@playwright/test";

test("should login and display user info", async ({ page }) => {
  await page.goto("/login");
  await page.getByPlaceholder("Nazwa użytkownika").fill("root");
  await page.getByPlaceholder("Hasło").fill("rootroot");
  await page.click("text=Zaloguj się");
  await page.waitForURL("/home");
  await page.goto("/bw"); // Redirect to Baza Wiedzy TODO: Click on the link when it's implemented
  await expect(page).toHaveURL("/bw");

  await expect(page.getByTestId("userinfo-container")).toContainText("root");
  await expect(
    page.getByTestId("userinfo-container").getByRole("img")
  ).toHaveAttribute("src", "/public/avatar/default.png");
});
