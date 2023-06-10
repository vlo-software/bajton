"use client";
import Link from "next/link";
import UserInfo from "@/components/userInfo";
import { useAuth } from "@/hooks/useAuth";

export default function Home() {
  const { userData, loading } = useAuth();
  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center p-24">
        <h1 className="text-6xl pb-12 font-bold">Dashboard</h1>
        <div className="w-96 h-14 bg-slate-200 dark:bg-slate-800">
          <UserInfo userData={userData} loading={loading} />
        </div>
        <Link className="text-blue-950" href="/dashboard/articles">
          Your articles
        </Link>
        <Link className="text-blue-950" href="/dashboard/courses">
          Your courses
        </Link>
        <Link className="text-blue-950" href="/dashboard/settings">
          Settings
        </Link>
        <Link className="text-blue-950" href="/">
          Home
        </Link>
      </main>
    </>
  );
}
