import Link from "next/link";

export default function Page({ params }: { params: { id: string } }) {
  return (
    <>
      <main className="flex min-h-screen flex-col items-center justify-center p-24">
        <h1 className="text-6xl pb-12 font-bold">Article {params.id}</h1>
        <Link className="text-blue-950" href="/search">
          Back
        </Link>
      </main>
    </>
  );
}
