import Link from "next/link";

export default function Page() {
  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center p-24">
        <h1 className="text-6xl pb-12 font-bold">Settings</h1>
        <Link className="text-blue-950" href={`/dashboard/`}>
          Back
        </Link>
      </main>
    </>
  );
}
