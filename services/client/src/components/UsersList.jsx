import React from "react";

const UsersList = ({ users }) => {
  return (
    <div className="space-y-4">
      {users.map((user) => (
        <div
          key={user.id}
          className="p-4 bg-white rounded-lg border border-gray-400 shadow-sm"
        >
          <h4 className="font-bold text-lg text-gray-800">{user.username}</h4>
          <p className="text-sm text-gray-500">{user.email}</p>
        </div>
      ))}
    </div>
  );
};

export default UsersList
