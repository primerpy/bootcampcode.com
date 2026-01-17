import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import axios from "axios";

const App = () => {
  const [users, setUsers] = useState([]);

  const getUsers = () => {
    const apiUrl = import.meta.env.VITE_APP_USERS_SERVICE_URL;
    axios
      .get(`${apiUrl}/users`)
      .then((res) => {
        setUsers(res.data.data.users);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getUsers();
  }, []);

  return (
    <div className="container mx-auto px-4 py-8 max-w-2xl">
      <header className="mb-8 border-b pb-4 border-gray-200">
        <h1 className="text-4xl font-extrabold text-blue-600 tracking-tight">
          All Users
        </h1>
      </header>
      <div className="space-y-4">
        {users.map((user) => (
          <div
            key={user.id}
            className="p-4 bg-white rounded-lg border border-gray-100 shadow-sm hover:shadow-md transition-shadow"
          >
            <h4 className="font-bold text-lg text-gray-800">{user.username}</h4>
            <p className="text-sm text-gray-500">{user.email}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
