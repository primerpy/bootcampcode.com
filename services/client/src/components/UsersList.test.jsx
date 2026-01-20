import React from 'react';
import { render, screen } from '@testing-library/react';
import UsersList from './UsersList';

const users = [
  { id: 1, username: 'primerpy', email: 'primerpy@primerpy.com' },
  { id: 2, username: 'primerpy2', email: 'primerpy2@primerpy.com' }
];

test('renders a list of users', () => {
  render(<UsersList users={users} />);

  // Check if usernames are rendered
  expect(screen.getByText('primerpy')).toBeInTheDocument();
  expect(screen.getByText('primerpy2')).toBeInTheDocument();

  // Check if emails are rendered
  expect(screen.getByText('primerpy@primerpy.com')).toBeInTheDocument();
});

test('renders snapshot correctly', () => {
  const { asFragment } = render(<UsersList users={users} />);
  expect(asFragment()).toMatchSnapshot();
});

