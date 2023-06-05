"use client";
import UserInfo from "@/components/userInfo";
import { useAuth } from "@/hooks/useAuth";
import Link from "next/link";

export default function Home() {
  const { userData, loading } = useAuth();
  console.log(userData, loading);
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-6xl pb-12 font-bold">Baza Wiedzy</h1>
      <Link className="text-blue-950" href="/dashboard">
        Dashboard
      </Link>
      {/* This div is just a placeholder to showcase the UserInfo component */}
      <div className="w-96 h-14 bg-slate-200 dark:bg-slate-800">
        <UserInfo userData={userData} loading={loading} />
      </div>
    </main>
  );
}
