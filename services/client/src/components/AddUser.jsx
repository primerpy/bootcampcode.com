import React from "react";

const AddUser = ({ addUser, username, email, handleChange }) => {
  return (
    <form
      onSubmit={(e) => addUser(e)}
      className="mb-10 bg-white p-6 rounded-xl shadow-sm border border-gray-200"
    >
      <h2 className="text-xl font-bold mb-4">Add New User</h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Username
          </label>
          <input
            type="text"
            name="username"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            placeholder="Enter a username"
            required
            value={username}
            onChange={handleChange}
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Email
          </label>
          <input
            type="email"
            name="email"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            placeholder="Enter an email address"
            required
            value={email}
            onChange={handleChange}
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold-py-3 rounded-lg shadow-md transition-colors"
        >
          Add User
        </button>
      </div>
    </form>
  );
};

export default AddUser;
