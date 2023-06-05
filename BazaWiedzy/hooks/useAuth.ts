"use client";
import { useEffect, useState } from "react";

export type UserData = {
  id: number;
  user: {
    id: number;
    email: string | null;
    username: string;
    admin_type: "Regular User" | "Admin" | "Super Admin";
    problem_permission: "All" | "Own" | "None";
    create_time: string;
    last_login: string | null;
  };
  real_name: string | null;
  avatar: string;
  language: "pl-PL" | "en-US";
  school: string | null;
};

export function useAuth() {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadUser = async () => {
      const response = await fetch("/api/profile");
      const data = await response.json();
      if (data.error || data.data === null) throw new Error(data.error); // User is not logged in
      setUserData(data.data);
      setLoading(false);
    };
    loadUser().catch((err) => {
      console.error(err);
      window.localStorage.setItem("authed", "false");
      window.location.href = "/login";
    });
  }, []);

  return { userData, loading };
}
