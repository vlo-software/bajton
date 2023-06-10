import Link from "next/link";

export default function Page() {
  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center p-24">
        <h1 className="text-6xl pb-12 font-bold">Articles:</h1>
        <Link className="text-blue-950" href="/articles/1">
          Article 1
        </Link>
        <Link className="text-blue-950" href="/articles/2">
          Article 2
        </Link>
        <h1 className="text-6xl pb-12 font-bold">Courses:</h1>
        <Link className="text-blue-950" href="/courses/1">
          Course 1
        </Link>
        <Link className="text-blue-950" href="/courses/2">
          Course 2
        </Link>
        <Link className="text-blue-950 mt-2" href="/">
          Home
        </Link>
      </main>
    </>
  );
}
