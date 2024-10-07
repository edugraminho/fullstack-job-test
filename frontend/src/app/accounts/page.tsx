"use client";

import { useState, useEffect } from "react";

export default function Accounts() {
  const [accounts, setAccounts] = useState<
    { id: string; name: string; document: string }[]
  >([]);
  const [accountType, setAccountType] = useState("PERSONAL");
  const [name, setName] = useState("");
  const [document, setDocument] = useState("");
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [accountStatement, setAccountStatement] =
    useState<AccountStatement | null>(null);
  const [statementMessage, setStatementMessage] = useState<string>("");
  const [totalBalance, setTotalBalance] = useState<number | null>(null);
  const [openAccounts, setOpenAccounts] = useState<Account[]>([]);

  interface AccountStatement {
    accountId: string;
    balance: number;
    transactions: {
      id: string;
      accountId: string;
      type: string;
      amount: number;
      description: string;
      recipientName?: string;
      recipientDocument?: string;
      recipientBank?: string;
      recipientBranch?: string;
      recipientAccount?: string;
      billetCode?: string | null;
      pixKey?: string | null;
      e2eId?: string | null;
      createdAt: string;
    }[];
  }

  interface Account {
    id: string;
    tenantId: string;
    account_type: "PERSONAL" | "BUSINESS";
    name: string;
    document: string;
    status: string;
    balance: number;
    branch: string;
    number: string;
    createdAt: string;
    updatedAt: string;
  }

  const login = async () => {
    try {
      const response = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const data = await response.json();
        setToken(data.access_token);
      } else {
        console.error("Login failed");
      }
    } catch (error) {
      console.error("Error during login:", error);
    }
  };

  useEffect(() => {
    login();
  }, []);

  async function fetchAccounts() {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:8000/accounts/open", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();

      setAccounts(data.open_accounts || []);
    } catch (error) {
      console.error("Failed to fetch accounts:", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if (token) {
      fetchAccounts();
    }
  }, [token]);

  const handleCreateAccount = async (e: React.FormEvent) => {
    e.preventDefault();
    const newAccount = { accountType, name, document };

    if (token) {
      try {
        setLoading(true);
        const response = await fetch("http://localhost:8000/accounts", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify(newAccount),
        });

        if (response.ok) {
          const account = await response.json();
          setAccounts([...accounts, account]);
          setName("");
          setDocument("");
          setAccountType("PERSONAL");
          fetchTotalBalance();
        } else {
          console.error("Failed to create account");
        }
      } catch (error) {
        console.error("Error creating account:", error);
      } finally {
        setLoading(false);
      }
    } else {
      console.error("No token available");
    }
  };

  const handleViewStatement = async (accountId: string) => {
    if (token) {
      try {
        const response = await fetch(
          `http://localhost:8000/accounts/${accountId}/statement`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.ok) {
          const statement = await response.json();
          console.log("Account statement:", statement);

          if (statement.transactions.length === 0) {
            setStatementMessage("No transactions available for this account.");
          } else {
            setAccountStatement(statement);
            setStatementMessage("");
          }
        } else {
          console.error("Failed to fetcsdsdsdh account statement");
          setStatementMessage("Account with expired access in API Mock");
        }
      } catch (error) {
        console.error("Error fetching accoudssdsdnt statement:", error);
        setStatementMessage("Account with expired access in API Mock");
      } finally {
        setLoading(false);
      }
    }
  };

  async function fetchTotalBalance() {
    try {
      const response = await fetch(
        "http://localhost:8000/accounts/total-balance",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.ok) {
        const data = await response.json();
        setTotalBalance(data.total_balance);
      } else {
        console.error("Failed to fetch total balance");
      }
    } catch (error) {
      console.error("Error fetching total balance:", error);
    }
  }

  useEffect(() => {
    if (token) {
      fetchTotalBalance();
    }
  }, [token]);

  const fetchOpenAccounts = async () => {
    if (token) {
      try {
        setLoading(true);
        const response = await fetch("http://localhost:8000/accounts/open", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (response.ok) {
          const data = await response.json();
          setOpenAccounts(data.open_accounts || []);
        } else {
          console.error("Failed to fetch accounts summary");
        }
      } catch (error) {
        console.error("Error fetching accounts:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="min-h-screen p-8">
      <h1 className="text-2xl font-bold mb-8">Accounts</h1>
      <h2 className="text-xl font-bold mb-4">Create Account</h2>

      <form onSubmit={handleCreateAccount} className="mb-8">
        <select
          value={accountType}
          onChange={(e) => setAccountType(e.target.value)}
          className="border p-2 mr-2 text-black "
        >
          <option value="PERSONAL">Personal</option>
          <option value="BUSINESS">Business</option>
        </select>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="border p-2 mr-2 text-black "
        />
        <input
          type="text"
          placeholder="Document"
          value={document}
          onChange={(e) => setDocument(e.target.value)}
          className="border p-2 mr-2 text-black "
        />
        <button
          type="submit"
          className="bg-blue-500 text-white p-2"
          disabled={!token || loading}
        >
          {loading ? "Loading..." : "Create Account"}
        </button>
      </form>

      <h2 className="text-xl font-bold mb-4">Account List</h2>
      <ul>
        {accounts.length > 0 ? (
          accounts.map((account) => (
            <li key={account.id}>
              {account.name} - {account.document}
              <button
                className="ml-4 bg-blue-500 text-white p-1 rounded"
                onClick={() => handleViewStatement(account.id)}
              >
                View Statement
              </button>
            </li>
          ))
        ) : (
          <li>No accounts available</li>
        )}
      </ul>

      {accountStatement && accountStatement.transactions.length > 0 ? (
        <div className="mt-8">
          <h3 className="text-xl font-bold mb-4">Account Statement</h3>
          <p>
            <strong>Account ID:</strong> {accountStatement.accountId}
          </p>
          <p>
            <strong>Balance:</strong> {accountStatement.balance}
          </p>
          <ul className="border-t border-gray-300 mt-4">
            {accountStatement.transactions.map((transaction) => (
              <li
                key={transaction.id}
                className="py-4 border-b border-gray-300"
              >
                <div>
                  <strong>Date:</strong>{" "}
                  {new Date(transaction.createdAt).toLocaleString()}
                </div>
                <div>
                  <strong>Type:</strong> {transaction.type}
                </div>
                <div>
                  <strong>Amount:</strong> ${transaction.amount.toFixed(2)}
                </div>
                <div>
                  <strong>Description:</strong>{" "}
                  {transaction.description || "No description"}
                </div>
                {transaction.recipientName && (
                  <div>
                    <strong>Recipient:</strong> {transaction.recipientName}
                  </div>
                )}
                {transaction.recipientDocument && (
                  <div>
                    <strong>Recipient Document:</strong>{" "}
                    {transaction.recipientDocument}
                  </div>
                )}
                {transaction.recipientBank && (
                  <div>
                    <strong>Recipient Bank:</strong> {transaction.recipientBank}{" "}
                    - {transaction.recipientBranch} /{" "}
                    {transaction.recipientAccount}
                  </div>
                )}
                {transaction.billetCode && (
                  <div>
                    <strong>Billet Code:</strong> {transaction.billetCode}
                  </div>
                )}
                {transaction.pixKey && (
                  <div>
                    <strong>PIX Key:</strong> {transaction.pixKey}
                  </div>
                )}
                {transaction.e2eId && (
                  <div>
                    <strong>End-to-End ID:</strong> {transaction.e2eId}
                  </div>
                )}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>
          {statementMessage ||
            "Click on 'View Statement' to see account details."}
        </p>
      )}
      <div className="mt-8">
        <h2 className="text-xl font-bold">Total Balance of All Accounts</h2>
        {totalBalance !== null ? (
          <p className="text-lg">Total Balance: ${totalBalance}.00</p>
        ) : (
          <p className="text-lg">Loading total balance...</p>
        )}
      </div>

      <div className="mt-12">
        <button
          onClick={fetchOpenAccounts}
          className="bg-green-500 text-white p-2 mb-4"
        >
          View Open Accounts Summary
        </button>
      </div>
      <div>
        <h2 className="text-xl font-bold mb-4 mt-4">Open Accounts Summary</h2>
        {loading ? (
          <p>Loading accounts...</p>
        ) : openAccounts.length > 0 ? (
          <ul>
            {openAccounts.map((account) => (
              <li className="mt-4" key={account.id}>
                <p>
                  <strong>Name:</strong> {account.name}
                </p>
                <p>
                  <strong>Account Type:</strong> {account.account_type}
                </p>
                <p>
                  <strong>Balance:</strong> ${account.balance}.00
                </p>
                <p>
                  <strong>Document:</strong> {account.document}
                </p>
                <p>
                  <strong>Status:</strong> {account.status}
                </p>
                <hr />
              </li>
            ))}
          </ul>
        ) : (
          <p>No open accounts found</p>
        )}
      </div>
    </div>
  );
}
