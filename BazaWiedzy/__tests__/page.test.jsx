import { render, screen } from "@testing-library/react";
import Page from "../app/page";
import "@testing-library/jest-dom";

describe("Home", () => {
  it("renders a heading", () => {
    render(<Page />);

    const heading = screen.getByRole("heading", {
      name: /Baza Wiedzy/i,
    });

    expect(heading).toBeInTheDocument();
  });
});
