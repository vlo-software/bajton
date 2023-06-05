import { render, screen } from "@testing-library/react";
import UserInfo from "../components/userInfo";
import "@testing-library/jest-dom";

const mockUserData = {
  user: {
    username: "test test",
  },
  real_name: "Test Test",
  avatar: "/public/avatar/default.png",
};

describe("UserInfo", () => {
  it("renders a username and an avatar", () => {
    render(<UserInfo loading={false} userData={mockUserData} />);

    const img = screen.getByRole("img");

    expect(img).toBeInTheDocument();
    expect(img).toHaveAttribute("alt", "user avatar");
    expect(img).toHaveAttribute("src", "/public/avatar/default.png");

    const username = screen.getByText("test test");

    expect(username).toBeInTheDocument();
  });
});
