import Link from "next/link";

export default function Home() {
  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center p-24">
        <h1 className="text-6xl pb-12 font-bold">Your articles:</h1>
        <div className="bg-slate-400 p-2 rounded-lg flex-row space-x-4">
          <Link className="text-blue-950" href="/dashboard/articles/1">
            Article 1
          </Link>
          <Link
            className="text-blue-950 bg-slate-300 p-1 rounded-lg"
            href="/dashboard/articles/1/editor"
          >
            Edit
          </Link>
        </div>
        <Link className="text-blue-950" href="/dashboard/articles/new">
          Create article
        </Link>
        <Link className="text-blue-950" href="/dashboard">
          Back
        </Link>
      </main>
    </>
  );
}
