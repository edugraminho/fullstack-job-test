"use client";
import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen p-8">
      <h1 className="text-2xl font-bold mb-8">Banking Dashboard</h1>
      <ul className="space-y-4">
        <li>
          <Link href="/accounts" className="text-blue-500 hover:underline">
            Manage Accounts
          </Link>
        </li>
      </ul>
    </div>
  );
}
