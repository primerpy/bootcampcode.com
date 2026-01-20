import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import axios from "axios";
import UsersList from "./components/UsersList";
import AddUser from "./components/AddUser";

const App = () => {
  const [users, setUsers] = useState([]);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");

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

  const handleChange = (event) => {
    const { name, value } = event.target;
    if (name === "username") setUsername(value);
    if (name === "email") setEmail(value);
  };

  const addUser = (event) => {
    event.preventDefault();
    const data = {
      username: username,
      email: email,
    };
    axios
      .post(`${import.meta.env.VITE_APP_USERS_SERVICE_URL}/users`, data)
      .then(() => {
        getUsers();
        setUsername("");
        setEmail("");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="container mx-auto px-4 py-8 max-w-2xl">
      <header className="mb-8 border-b pb-4 border-gray-200">
        <h1 className="text-4xl font-extrabold text-blue-600 tracking-tight">
          All Users
        </h1>
      </header>
      <AddUser
        addUser={addUser}
        username={username}
        email={email}
        handleChange={handleChange}
      />
      <UsersList users={users} />
    </div>
  );
};

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
